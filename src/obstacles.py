import sys
import src.shared as shared

class Obstacles() :

    def __init__(self) :

        self.obstaclePos = [ 2000, 6000, 12000 ]
        #self.obstaclePos = [ ]

        self.sprites = shared.assetsdb["obstacles"]
        self.width, self.height = self.sprites[0].get_size()

    def update(self) :

        if (not shared.character.collides()) :
            return

        for x in self.obstaclePos :
            if (abs(shared.character.pos - x) < (shared.character.width()/2 +
                self.width/2) * 0.65) :
                shared.character.die()

    def render(self) :

        for x in self.obstaclePos :

            if (abs(shared.character.pos - x) > shared.screenSize[0]) :
                continue

            shared.game.screen.blit(self.sprites[0], (shared.screenSize[0]/4 + x -
                shared.character.pos - self.width/2,410))




