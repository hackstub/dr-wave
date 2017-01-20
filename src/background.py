
import src.shared as shared

class Background() :

    def __init__(self) :

        self.pieces = [ shared.imagedb["bg0"] ]

        # Dunno what to do with this but we'll see lol
        self.currentPos = 0

    def update(self) :

        pass


    def render(self) :

        shared.game.screen.fill((220,220,250))
        shared.game.screen.blit(self.pieces[self.currentPos], (0,0))




