import pygame
from pygame.locals import *


#debug = False
debug = True

###############################################################################
#   Global parameters / configuration                                         #
###############################################################################

screenSize = (1000,700)

###############################################################################
#   Global assets                                                             #
###############################################################################

imagedb = { }

runLeft  = None
runRight = None

def loadAssets() :

    imagedb["bg0"] = pygame.image.load("assets/bg0.png")
    imagedb["bg0"].set_colorkey((255,0,254))

    global runLeft
    global runRight
    runLeft = Sequence()
    runRight = Sequence()
   
    runImage = pygame.image.load("assets/spriterun.png")
    runLeft .load(runImage, (225,225), 4, (None, 0))
    runRight.load(runImage, (225,225), 4, (None, 1))

    for image in imagedb.values() :
        image.convert_alpha()


###############################################################################
#   Cooldown                                                                  #
###############################################################################

import random

class Cooldown:

    def __init__(self, duration, randomness=0) :

        self.duration = duration
        self.randomness = randomness

        self.restart()

    def restart(self) :

        self.c = self.duration + random.randint(-self.randomness,self.randomness)

    def active(self) :

        return (self.c > 0)

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


