import sys
import src.shared as shared

class Obstacles() :

    def __init__(self) :

        self.obstaclePos = [ 2000, 6000, 12000 ]
        #self.obstaclePos = [ ]

        self.plateformePos = [];         self.plateformeType = [];
        for x in [ 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750] :
            self.plateformePos.append(x); self.plateformeType.append(0);


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

        for i, xp in enumerate(self.plateformePos) :

            t = self.plateformeType[i]
            w, h = shared.assetsdb["plateformes"][t].get_size()

            if (x > xp - w/2) and (x < xp + w /2) : 
                return True

        return False

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

            t = self.plateformeType[i]
            w, h = shared.assetsdb["plateformes"][t].get_size()

            shared.game.screen.blit(shared.assetsdb["plateformes"][t], (shared.screenSize[0]/4 + x -
                shared.character.pos - w/2,350))






