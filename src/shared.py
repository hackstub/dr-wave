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

def loadAssets() :
    assetsdb["title"]     = pygame.image.load("assets/menu/title.png")
    assetsdb["menu_play"] = pygame.image.load("assets/menu/play.png")
    assetsdb["menu_quit"] = pygame.image.load("assets/menu/quit.png")
    
    assetsdb["0"] = pygame.image.load("assets/timer/0.png")
    assetsdb["1"] = pygame.image.load("assets/timer/1.png")
    assetsdb["2"] = pygame.image.load("assets/timer/2.png")
    assetsdb["3"] = pygame.image.load("assets/timer/3.png")
    assetsdb["4"] = pygame.image.load("assets/timer/4.png")
    assetsdb["5"] = pygame.image.load("assets/timer/5.png")
    assetsdb["6"] = pygame.image.load("assets/timer/6.png")
    assetsdb["7"] = pygame.image.load("assets/timer/7.png")
    assetsdb["8"] = pygame.image.load("assets/timer/8.png")
    assetsdb["9"] = pygame.image.load("assets/timer/9.png")
    
    assetsdb["bg"] = []
    for i in range(8) :
        assetsdb["bg"].append(pygame.image.load("assets/background/"+str(i)+".png"))
        assetsdb["bg"][i].convert_alpha()
    
    assetsdb["seauley"] = pygame.image.load("assets/seauley.png")
    assetsdb["bottomline"] = pygame.image.load("assets/ligne.png")
    
    assetsdb["block"] = pygame.image.load("assets/block.png")
    assetsdb["block"].convert_alpha()

    assetsdb["characterrun"] = Sequence(reverseLoop=True)
    characterrun = pygame.image.load("assets/perso/run.png")
    assetsdb["characterrun"].load(characterrun, (283,283), 5, (None, 0))

    assetsdb["charactertransfo"] = Sequence()
    charactertransfo = pygame.image.load("assets/perso/transfo.png")
    assetsdb["charactertransfo"].load(charactertransfo, (283,283), 7, (None, 0))
 
    assetsdb["charactermort"] = Sequence()
    charactermort = pygame.image.load("assets/perso/mort.png")
    assetsdb["charactermort"].load(charactermort, (283,350), 4, (None, 0))
       
    #global runLeft
    #global runRight
    #runLeft = Sequence()
    #runRight = Sequence()
   
    #runImage = pygame.image.load("assets/spriterun.png")
    #runLeft .load(runImage, (225,225), 4, (None, 1))
    #runRight.load(runImage, (225,225), 4, (None, 0))


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



