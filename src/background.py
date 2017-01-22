import src.shared as shared

class Background() :

    def __init__(self) :

        self.bg0 = shared.assetsdb["bg0"]
        self.bg1 = shared.assetsdb["bg1"]
        self.bg2 = shared.assetsdb["bg2"]
        self.bg3 = shared.assetsdb["bg3"]
        
        self.line    = shared.assetsdb["bottomline"]
        self.seauley = shared.assetsdb["seauley"]
       
        self.weirdEffectParam = 0

    def update(self) :

        pass

    def render(self) :

        charpos = shared.character.pos

        if (not shared.character.wavemode()) :
        
            shared.game.screen.fill((0,240,240))
            shared.game.screen.blit(self.bg3,     (0,0))
            shared.game.screen.blit(self.seauley, (1000,40))
            
            self.render2At(charpos+1)
            self.render1At(charpos+1)
            self.render0At(charpos+1)

            self.weirdEffectParam = 0
        else :
           
            wea = self.weirdEffectParam
            if (wea > 10) : 
                wea = 20 - wea
        
            shared.game.screen.fill((wea*13,150-wea*wea,150-wea*13))
            shared.game.screen.blit(self.bg3,     (0,0))
            shared.game.screen.blit(self.seauley, (1000,40))
            
            for i in range(0, wea) :
                i = wea - i
                self.render2At(charpos - i*i*4)
            for i in range(0, wea) :
                i = wea - i
                self.render1At(charpos - i*i*4)
            for i in range(0, wea) :
                i = wea - i
                self.render0At(charpos - i*i*4)

            self.weirdEffectParam += 1
        
        shared.game.screen.blit(self.line, (0,0))

    def render0At(self, pos) :

        self.renderLayerAt(pos/2,   self.bg0)

    def render1At(self, pos) :

        self.renderLayerAt(pos/4, self.bg1)

    def render2At(self, pos) :

        self.renderLayerAt(pos/8, self.bg2)

    def renderLayerAt(self, pos, bg) :

        bgwidth = bg.get_size()[0]
        while (pos > bgwidth) :
            pos -= bgwidth

        shared.game.screen.blit(bg, (-pos,0))
        
        if (-pos + bgwidth < shared.screenSize[0]) :
            shared.game.screen.blit(bg, (-pos+bgwidth,0))



