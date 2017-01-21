
import src.shared as shared

class Background() :

    def __init__(self) :

        self.pieces = shared.imagedb["bg"]

        # Dunno what to do with this but we'll see lol
        self.currentPos = 0

    def update(self) :

        self.currentPos -= shared.characterSpeed

    def render(self) :

        merp = shared.screenSize[0]/1.3

        n = -1 * int(self.currentPos / merp)
        print(n)

        shared.game.screen.fill((0,220,0))
        for i in range(n,n+3):
            iBg = i % len(self.pieces)
            shared.game.screen.blit(self.pieces[iBg], (self.currentPos+i*merp,0))




