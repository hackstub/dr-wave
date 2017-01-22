import sys
import src.shared as shared

class Obstacles() :

    def __init__(self) :

        # Obstacle 

        self.obstaclePos  = [ ]
        self.obstacleType = [ ] 
        self.obstacleLevel = [ ] 
        self.plateformePos = [];         
        self.plateformeType = [];

        self.passerelleFromTo(2500,4500)
        
        self.addObstacle(1000,3)
        self.addObstacle(2500,5)
        self.addObstacle(4000,4)
        self.addObstacle(5500,6)
        self.addObstacle(7000,7)
        self.addObstacle(8500,0)

        self.sprites = shared.assetsdb["obstacles"]
        self.width, self.height = self.sprites[0].get_size()

    def update(self) :

        if (not shared.character.collides()) :
            return

        for i, x in enumerate(self.obstaclePos) :
            
            if (abs(self.obstacleLevel[i] - shared.character.floor) > 0.2) :
                continue

            t    = self.obstacleType[i]
            w, h = self.sprites[i].get_size()

            if (abs(shared.character.pos - x) < (shared.character.width()/2 + w/2) * 0.65) :
                shared.character.die()
    
    def addObstacle(self, x, t, level = 0) :

        self.obstaclePos.append(x);
        self.obstacleType.append(t);
        self.obstacleLevel.append(level);

    def passerelleFromTo(self, begin, end) :
    
         x = 0
         while (x < end - begin) :
            self.plateformePos.append(begin+x); self.plateformeType.append(0);
            x += 250


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

        for i, x in enumerate(self.obstaclePos) :

            if (abs(shared.character.pos - x) > 2*shared.screenSize[0]) :
                continue
            
            t = self.obstacleType[i]

            shared.game.screen.blit(self.sprites[t], (shared.screenSize[0]/4 + x -
                shared.character.pos - self.width/2,450))

        for i, x in enumerate(self.plateformePos) :

            if (abs(shared.character.pos - x) > 2*shared.screenSize[0]) :
                continue

            t = self.plateformeType[i]
            w, h = shared.assetsdb["plateformes"][t].get_size()

            shared.game.screen.blit(shared.assetsdb["plateformes"][t], (shared.screenSize[0]/4 + x -
                shared.character.pos - w/2,350))






