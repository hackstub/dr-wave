import sys
import src.shared as shared

class Obstacles() :

    def __init__(self) :

        self.obstaclePos = [ 2000, 6000, 12000 ]
        #self.obstaclePos = [ ]

        self.plateformePos  = [ 2000, 6000, 12000 ]
        self.plateformeType = [ 0,    1,    2     ]



        self.sprites = shared.assetsdb["obstacles"]
        self.width, self.height = self.sprites[0].get_size()

    def update(self) :

        if (not shared.character.collides()) :
            return

        if (shared.character.floor == 1) :
            return

        for x in self.obstaclePos :
            if (abs(shared.character.pos - x) < (shared.character.width()/2 +
                self.width/2) * 0.65) :
                shared.character.die()
    
    def plateformeAtX(self, x) :

        pass

    def obstacleAtX(self, x) :
    
        pass
        

    def render(self) :

        for x in self.obstaclePos :

            if (abs(shared.character.pos - x) > 2*shared.screenSize[0]) :
                continue

            shared.game.screen.blit(self.sprites[0], (shared.screenSize[0]/4 + x -
                shared.character.pos - self.width/2,450))

        for i, x in enumerate(self.plateformePos) :

            if (abs(shared.character.pos - x) > 2*shared.screenSize[0]) :
                continue

            w, h = shared.assetsdb["plateformes"][i].get_size()

            shared.game.screen.blit(shared.assetsdb["plateformes"][i], (shared.screenSize[0]/4 + x -
                shared.character.pos - w/2,350))






