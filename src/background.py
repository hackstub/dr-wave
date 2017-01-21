
import src.shared as shared

class Background() :

    def __init__(self) :

        self.pieces = shared.imagedb["bg"]

    def update(self) :

        pass

    def render(self) :

        bgWidth = shared.screenSize[0]/1.3

        n = int(shared.character.pos / bgWidth)

        shared.game.screen.fill((0,220,0))
        for i in range(n,n+3):
            iBg = i % len(self.pieces)
            shared.game.screen.blit(self.pieces[iBg], (i*bgWidth-shared.character.pos,0))




