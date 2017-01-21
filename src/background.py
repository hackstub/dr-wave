
import src.shared as shared

class Background() :

    def __init__(self) :

        self.pieces = shared.assetsdb["bg"]
        
        self.line = shared.assetsdb["bottomline"]
       
        self.piecesEdges = []
        x = 0
        self.piecesEdges.append(0)
        for i in range(len(self.pieces)) :
            w,h = self.pieces[i].get_size()
            x += w
            self.piecesEdges.append(x)

        self.weirdEffectParam = 0

    def update(self) :

        pass

    def render(self) :

        charpos = shared.character.pos
        shared.game.screen.fill((0,0,0))

        if (shared.character.collides()) :
            self.renderAt(charpos)
            self.weirdEffectParam = 0
        else :
            
            for i in range(0, self.weirdEffectParam) :
                i = self.weirdEffectParam - i
                self.renderAt(charpos - i*(i*0.2 + 0.1 * self.weirdEffectParam*self.weirdEffectParam))
            self.weirdEffectParam += 1
        
        shared.game.screen.blit(self.line, (0,0))

    def renderAt(self, pos) :

        allPiecesWidth = self.piecesEdges[len(self.piecesEdges) - 1]

        for i, piece in enumerate(self.pieces) :
            leftEdge  = self.piecesEdges[i]   - pos
            rightEdge = self.piecesEdges[i+1] - pos

            while (rightEdge < 0) :
                leftEdge  += allPiecesWidth
                rightEdge += allPiecesWidth

            if (((leftEdge  > 0) and (leftEdge  < shared.screenSize[0]))
             or ((rightEdge > 0) and (rightEdge < shared.screenSize[0]))
             or ((leftEdge < 0) and (rightEdge > shared.screenSize[0]))) :
            
                shared.game.screen.blit(piece, (leftEdge,0))

