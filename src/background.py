import src.shared as shared

class Background() :

    def __init__(self) :

        self.pieces0  = shared.assetsdb["bg0"]
        self.pieces1  = shared.assetsdb["bg1"]
        self.pieces2  = shared.assetsdb["bg2"]
        self.globalbg = shared.assetsdb["bg3"]
        
        self.line    = shared.assetsdb["bottomline"]
        self.seauley = shared.assetsdb["seauley"]
       
        self.pieces0Edges = self.piecesEdges(self.pieces0)
        self.pieces1Edges = self.piecesEdges(self.pieces1)
        self.pieces2Edges = self.piecesEdges(self.pieces2)

        self.weirdEffectParam = 0

        self.allPiecesWidth0 = self.pieces0Edges[len(self.pieces0Edges) - 1]
        self.allPiecesWidth1 = self.pieces1Edges[len(self.pieces1Edges) - 1]
        self.allPiecesWidth2 = self.pieces2Edges[len(self.pieces2Edges) - 1]

    def piecesEdges(self, pieces) :

        out = [ ]
        x = 0
        out.append(x)

        for piece in pieces :
            w,h = piece.get_size()
            x += w
            out.append(x)

        return out

    def update(self) :

        pass

    def render(self) :

        charpos = shared.character.pos

        if (shared.character.collides()) :
        
            shared.game.screen.fill((0,240,240))
            shared.game.screen.blit(self.globalbg, (0,0))
            shared.game.screen.blit(self.seauley, (1000,40))
            
            self.renderAt(charpos)
            self.weirdEffectParam = 0
        else :
           
            wea = self.weirdEffectParam
            if (wea > 10) : 
                wea = 20 - wea
        
            shared.game.screen.fill((wea*13,150-wea*wea,150-wea*13))
            shared.game.screen.blit(self.globalbg, (0,0))
            shared.game.screen.blit(self.seauley, (1000,40))
            
            for i in range(0, wea) :
                i = wea - i
                self.renderAt(charpos - i*i*4)
            self.weirdEffectParam += 1
        
        shared.game.screen.blit(self.line, (0,0))

    def renderAt(self, pos) :

        self.renderLayerAt(pos/4, self.pieces2, self.pieces2Edges, self.allPiecesWidth2)
        self.renderLayerAt(pos/2, self.pieces1, self.pieces1Edges, self.allPiecesWidth1)
        self.renderLayerAt(pos,   self.pieces0, self.pieces0Edges, self.allPiecesWidth0)

    def renderLayerAt(self, pos, pieces, edges, allwidth) :

        for i, piece in enumerate(pieces) :
            leftEdge  = edges[i]   - pos
            rightEdge = edges[i+1] - pos

            # Trick to loop all pieces
            while (rightEdge < 0) :
                leftEdge  += allwidth
                rightEdge += allwidth

            if (((leftEdge  > 0) and (leftEdge  < shared.screenSize[0]))
             or ((rightEdge > 0) and (rightEdge < shared.screenSize[0]))
             or ((leftEdge  < 0) and (rightEdge > shared.screenSize[0]))) :
            
                shared.game.screen.blit(piece, (leftEdge,0))



