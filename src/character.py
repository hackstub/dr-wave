
import src.shared as shared

class Character() :

    def __init__(self) :

        self.runRight = shared.runRight
        self.runRight.setCooldown(5)

    def update(self) :

        self.runRight.tick()

    def render(self) :

        shared.game.screen.blit(self.runRight.getCurrentSprite(), (450,500))




