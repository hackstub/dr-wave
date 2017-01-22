
import pygame
from pygame.locals import *

import math
from enum import Enum

import sys

import src.shared as shared

class CharacterState(Enum) :
    SOLID = 0
    WAVE = 1
    MORPH_TO   = 2
    MORPH_BACK = 3
    DEAD = 4


class Character() :

    def __init__(self) :

        self.run = shared.assetsdb["run"]
        self.run.setCooldown(1)
   
        self.morph = shared.assetsdb["morph"]
        self.morph.setCooldown(1)

        self.dead = shared.assetsdb["die"]
        self.dead.setCooldown(4)

        self.pos = 0

        self.status = CharacterState.SOLID
    
        self.waveStateCD = shared.Cooldown(10, start=False)
        self.morphDisabledCD = shared.Cooldown(10, start=False)
        
        self.speedUp = shared.Cooldown(30)
        self.speedUpFactor = 1.0

        self.floor = 0

        # Loading sounds
        self.dashLoadingSound = pygame.mixer.Sound("sounds/dash-charge.ogg")
        self.dashSound = pygame.mixer.Sound("sounds/dash.ogg")
        self.crashSound = pygame.mixer.Sound("sounds/run-end.ogg")

    def update(self) :

        self.waveStateCD.tick()
        self.morphDisabledCD.tick()
        self.speedUp.tick()
        
        if (self.status == CharacterState.SOLID) :
            self.run.tick()

        elif (self.status == CharacterState.MORPH_TO) :
            idBefore = self.morph.currentId
            self.morph.tick()
            idAfter = self.morph.currentId
            if (idAfter < idBefore) :
                self.doneMorphingTo()

        elif (self.status == CharacterState.MORPH_BACK) :
            idBefore = self.morph.currentId
            self.morph.tick()
            idAfter = self.morph.currentId
            if (idAfter > idBefore) :
                self.doneMorphingBack()

        elif (self.status == CharacterState.DEAD) :
            idBefore = self.dead.currentId
            self.dead.tick()
            idAfter = self.dead.currentId
            if (idAfter < idBefore) :
                print("Game over lol")
                sys.exit(-1)

        if (self.waveStateCD.justStopped()) :
            self.status = CharacterState.SOLID
            #self.waveStateCD = shared.Cooldown(int(15/self.speedUpFactor), start=False)
            
            self.status = CharacterState.MORPH_BACK
            self.morph.setCurrentSprite(len(self.morph.sprites) - 1)
            self.morph.reverseLoop = True

        if (self.speedUp.justStopped()) :
            self.speedUp.restart()
            self.speedUpFactor += 0.01

        self.pos += self.speed()
        
        
    def speed(self) :

        if (self.status == CharacterState.SOLID) :
            return 20*self.speedUpFactor
        if (self.status == CharacterState.MORPH_TO) :
            return (20 + 40 * self.morph.currentId/len(self.morph.sprites))*self.speedUpFactor
        if (self.status == CharacterState.MORPH_BACK) :
            return (20 + 40 * self.morph.currentId/len(self.morph.sprites))*self.speedUpFactor
        if (self.status == CharacterState.WAVE) :
            return 60*self.speedUpFactor
        else :
            return 0

    def width(self) :
        
        sprite = self.run.getCurrentSprite()
        width, height = sprite.get_size()
        return width
        
    def wavemode(self) : 
        return (self.status == CharacterState.WAVE)

    def collides(self) :

        if (self.status == CharacterState.WAVE) : return False
        if ((self.status == CharacterState.MORPH_TO) and
        (self.morph.currentId/len(self.morph.sprites) > 0.5)) : return False
        if ((self.status == CharacterState.MORPH_BACK) and
        (self.morph.currentId/len(self.morph.sprites) < 0.5)) : return False

        return True


    def die(self) :
        
        if (self.status == CharacterState.DEAD) :
            self.crashSound.play()
            return

        self.status = CharacterState.DEAD
        
        self.dead.setCurrentSprite(0)


    def render(self) :

        if (self.status == CharacterState.WAVE) :
            return
        elif (self.status == CharacterState.MORPH_TO) :
            sprite = self.morph.getCurrentSprite()
        elif (self.status == CharacterState.MORPH_BACK) :
            sprite = self.morph.getCurrentSprite()
        elif (self.status == CharacterState.DEAD) :
            sprite = self.dead.getCurrentSprite()
        else :
            sprite = self.run.getCurrentSprite()
        
        width, height = sprite.get_size()

        shared.game.screen.blit(sprite, (shared.screenSize[0] / 4 - width/2,
                                         shared.screenSize[1] - 30 - self.floor * 200 - height))


    def doneMorphingTo(self) :

        self.status = CharacterState.WAVE
        self.dashLoadingSound.play()
        self.waveStateCD.restart()

    def doneMorphingBack(self) :

        self.status = CharacterState.SOLID
        self.dashSound.play()
        self.morphDisabledCD.restart()
         
    def handleMorphKey(self) :

        if ((self.status == CharacterState.WAVE)
        or (self.status == CharacterState.MORPH_TO)
        or (self.morphDisabledCD.active())) :
            return

        shared.game.screen.fill((0,0,0))
        self.status = CharacterState.MORPH_TO
        self.morph.setCurrentSprite(0)
        self.morph.reverseLoop = False

        if (pygame.key.get_pressed()[pygame.K_UP]) :
            self.floor += 1
        if (pygame.key.get_pressed()[pygame.K_DOWN]) :
            self.floor -= 1

        if (self.floor <  0) : self.floor = 0
        if (self.floor >= 1) : self.floor = 1



