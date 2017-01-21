
import src.shared as shared

from enum import Enum

class CharacterState(Enum) :
    SOLID = 0
    WAVE = 1


class Character() :

    def __init__(self) :

        self.runRight = shared.runRight
        self.runRight.setCooldown(5)

        self.pos = 0

        self.status = CharacterState.SOLID
    
        self.transformCD = shared.Cooldown(15, start=False)
        self.transformDisabledCD = shared.Cooldown(10, start=False)
        
        self.speedUp = shared.Cooldown(10)
        self.speedUpFactor = 1.0

    def update(self) :

        self.runRight.tick()
        self.transformCD.tick()
        self.transformDisabledCD.tick()
        self.speedUp.tick()

        if (self.transformCD.justStopped()) :
            self.status = CharacterState.SOLID
            #self.transformCD = shared.Cooldown(int(15/self.speedUpFactor), start=False)
            self.transformDisabledCD.restart()

        if (self.speedUp.justStopped()) :
            self.speedUp.restart()
            self.speedUpFactor += 0.01

        self.pos += self.speed()

    def speed(self) :

        if (self.status == CharacterState.SOLID) :
            return 10*self.speedUpFactor
        if (self.status == CharacterState.WAVE) :
            return 20*self.speedUpFactor

    def width(self) :
        
        sprite = self.runRight.getCurrentSprite()
        width, height = sprite.get_size()
        return width

    def collides(self) :

        return False
        return (self.status == CharacterState.SOLID)

    def render(self) :

        if (self.status == CharacterState.WAVE) :
            return

        sprite = self.runRight.getCurrentSprite()
        width, height = sprite.get_size()

        shared.game.screen.blit(sprite, (shared.screenSize[0] / 2 - width / 2,500))

    def handleTransformKey(self) :

        if (self.status == self.status.WAVE) :
            return
        
        if (self.transformDisabledCD.active()) :
            return

        self.status = CharacterState.WAVE        
        self.transformCD.restart()



