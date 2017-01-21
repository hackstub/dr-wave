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

imagedb = { }

runLeft  = None
runRight = None

def loadAssets() :

    imagedb["bg"] = []
    for i in range(5) :
        imagedb["bg"].append(pygame.image.load("assets/backgrounds/"+str(i)+".jpg"))
        imagedb["bg"][i].convert_alpha()
    
    imagedb["block"] = pygame.image.load("assets/block.png")
    imagedb["block"].convert_alpha()

    #imagedb["bg"].set_colorkey((255,0,254))

    global runLeft
    global runRight
    runLeft = Sequence()
    runRight = Sequence()
   
    runImage = pygame.image.load("assets/spriterun.png")
    runLeft .load(runImage, (225,225), 4, (None, 1))
    runRight.load(runImage, (225,225), 4, (None, 0))


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

    def __init__(self) :

        self.sprites = [ ]

        self.currentId = -1

        self.cd = None

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

        self.currentId += 1

        if (self.currentId >= len(self.sprites)) :
            self.currentId = 0

    def setCooldown(self, duration, randomness=0) :

        self.cooldown = Cooldown(duration, randomness)

    def tick(self) : 
        
        self.cooldown.tick()
    
        if (not self.cooldown.active()) :
            self.goNextSprite()
            self.cooldown.restart()


