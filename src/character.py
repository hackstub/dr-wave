
import src.shared as shared

class Character() :

    def __init__(self) :

        self.runRight = shared.runRight
        self.runRight.setCooldown(5)

        self.pos = 0

    def update(self) :

        self.runRight.tick()
        
        self.pos += shared.characterSpeed

    def width(self) :
        
        sprite = self.runRight.getCurrentSprite()
        width, height = sprite.get_size()
        return width

    def render(self) :

        sprite = self.runRight.getCurrentSprite()
        width, height = sprite.get_size()

        shared.game.screen.blit(sprite, (shared.screenSize[0] / 2 - width / 2,500))




