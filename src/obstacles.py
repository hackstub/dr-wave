import sys
import src.shared as shared

class Obstacles() :

    def __init__(self) :

        self.obstaclePos = [ 500 ]

        self.sprite = shared.imagedb["block"]
        self.width, self.height = self.sprite.get_size()

    def update(self) :

        if (not shared.character.collides()) :
            return

        for x in self.obstaclePos :
            if (abs(shared.character.pos - x) < (shared.character.width()/2 +
                self.width/2) * 0.65) :
                print("Game over wesh")
                sys.exit(-1)

    def render(self) :

        for x in self.obstaclePos :

            if (abs(shared.character.pos - x) > shared.screenSize[0]) :
                continue

            shared.game.screen.blit(self.sprite, (shared.screenSize[0]/2 + x -
                shared.character.pos - self.width/2,610))




