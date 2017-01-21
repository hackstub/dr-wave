
import src.shared as shared

class Obstacles() :

    def __init__(self) :

        self.obstaclePos = [ 500 ]

    def update(self) :

        pass

    def render(self) :

        for x in self.obstaclePos :

            if (abs(shared.character.pos - x) > shared.screenSize[0]) :
                continue

            shared.game.screen.blit(shared.imagedb["block"],
                    (shared.screenSize[0]/2 + x - shared.character.pos,610))




