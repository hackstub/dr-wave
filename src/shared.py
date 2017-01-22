import pygame
from pygame.locals import *

###############################################################################
#   Global parameters / configuration                                         #
###############################################################################

#debug = False
debug = True

screenSize = (1280,720)

###############################################################################
#   Global assets                                                             #
###############################################################################

assetsdb = { }

runLeft  = None
runRight = None

def mergeBg(bgs) :

    w = 0
    for bg in bgs :
        w += bg.get_size()[0]
    h = bgs[0].get_size()[1]

    out = pygame.Surface((w, h), SRCALPHA)
    x = 0
    for bg in bgs :
        out.blit(bg, (x, 0))
        x   += bg.get_size()[0]

    return out

def loadAssets() :
    assetsdb["title"]     = pygame.image.load("assets/interface/title.png")
    assetsdb["menu_play"] = pygame.image.load("assets/interface/play.png")
    assetsdb["menu_quit"] = pygame.image.load("assets/interface/quit.png")
    assetsdb["menu_retry"] = pygame.image.load("assets/interface/retry.png")
    assetsdb["over"] = pygame.image.load("assets/interface/gameOver.png")
    
    assetsdb["timer_box"] = pygame.image.load("assets/interface/timerbox.png")

    assetsdb["timer_digits"] = Sequence()
    timer_digits = pygame.image.load("assets/interface/digits.png")
    assetsdb["timer_digits"].load(timer_digits, (22,30), 10, (None, 0))

    assetsdb["bg0"] = []
    assetsdb["bg1"] = []
    assetsdb["bg2"] = []
    for i in range(6) :
        assetsdb["bg0"].append(pygame.image.load("assets/bg0/"+str(i)+".png"))
        assetsdb["bg0"][i].convert_alpha()
    for i in range(7) :
        assetsdb["bg1"].append(pygame.image.load("assets/bg1/"+str(i)+".png"))
        assetsdb["bg1"][i].convert_alpha()
    for i in range(5) :
        assetsdb["bg2"].append(pygame.image.load("assets/bg2/"+str(i)+".png"))
        assetsdb["bg2"][i].convert_alpha()
  
    assetsdb["bg0"] = mergeBg(assetsdb["bg0"]) 
    assetsdb["bg1"] = mergeBg(assetsdb["bg1"]) 
    assetsdb["bg2"] = mergeBg(assetsdb["bg2"]) 
    assetsdb["bg3"] = pygame.image.load("assets/bg3.png")

    assetsdb["seauley"] = pygame.image.load("assets/seauley.png")
    assetsdb["bottomline"] = pygame.image.load("assets/ligne.png")
    
    assetsdb["obstacles"] = []
    for i in range(10) :
        assetsdb["obstacles"].append(pygame.image.load("assets/obstacles/"+str(i)+".png"))
        assetsdb["obstacles"][i].convert_alpha()

    assetsdb["plateformes"] = []
    for i in range(3) :
        assetsdb["plateformes"].append(pygame.image.load("assets/plateformes/large"+str(i)+".png"))
        assetsdb["plateformes"][i].convert_alpha()

    assetsdb["run"] = Sequence(reverseLoop=True)
    run = pygame.image.load("assets/perso/run.png")
    assetsdb["run"].load(run, (283,283), 5, (None, 0))

    assetsdb["morph"] = Sequence()
    morph = pygame.image.load("assets/perso/morph.png")
    assetsdb["morph"].load(morph, (283,283), 7, (None, 0))
 
    assetsdb["die"] = Sequence()
    die = pygame.image.load("assets/perso/die.png")
    assetsdb["die"].load(die, (283,350), 4, (None, 0))

    assetsdb["star"] = pygame.image.load("assets/star.png")
       
###############################################################################
#   Cooldown                                                                  #
###############################################################################

import random

class Cooldown:

    def __init__(self, duration, randomness=0, start=True) :

        self.duration = duration
        self.randomness = randomness

        self.c = 0

        if (start) :
            self.restart()

    def restart(self) :

        self.c = self.duration + random.randint(-self.randomness,self.randomness)

    def active(self) :

        return (self.c > 0)

    def justStopped(self) :

        return (self.c == 0)

    def tick(self) :

        self.c -= 1

###############################################################################
#   Sequence                                                                  #
###############################################################################

class Sequence:

    def __init__(self, reverseLoop=False) :

        self.sprites = [ ]

        self.currentId = -1

        self.cd = None

        self.reverseLoop = reverseLoop
        self.order = 1

    def load(self, img, spriteSize, n, offset) :
        
        offset_x, offset_y = offset

        if (offset_x == None) and (offset_y == None) :
            print("Error, specify at least offset_x or offset_y when loading sequence")
            return

        self.sprites = [ ]

        w, h = spriteSize

        for i in range(n) :
            if (offset_x == None) :
                x, y = (i, offset_y)
            else :
                x, y = (offset_x, i)

            self.sprites.append(img.subsurface((x*w, y*h, w, h)))

    def setCurrentSprite(self, i) :

        self.currentId = i
    
    def getCurrentSprite(self) :

        return self.sprites[self.currentId]
    
    def goNextSprite(self) :

        if (self.order == 1) :
            self.currentId += 1
        else :
            self.currentId -= 1

        if (self.currentId >= len(self.sprites)) :

            if (self.reverseLoop) :
                self.order = -1
                self.currentId += -2
            else :
                self.currentId = 0

        elif (self.currentId < 0) :
            
            if (self.reverseLoop) :
                self.currentId += 2
                self.order = 1
        

    def setCooldown(self, duration, randomness=0) :

        self.cooldown = Cooldown(duration, randomness)

    def tick(self) : 
        
        self.cooldown.tick()
    
        if (not self.cooldown.active()) :
            self.goNextSprite()
            self.cooldown.restart()



