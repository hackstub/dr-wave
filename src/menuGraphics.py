import pygame, math

import src.shared as shared

class MenuGraphics() :

    def __init__(self) :

        self.title = shared.assetsdb["title"]
        self.play  = shared.assetsdb["menu_play"]
        self.quit  = shared.assetsdb["menu_quit"]
        self.retry = shared.assetsdb["menu_retry"]
        
        pass

    def update(self) :

        pass

    def render(self, idx, dy) :
        shared.game.screen.blit(shared.assetsdb["bottomline"], (0,0))

        t = 1000*pygame.time.get_ticks()
        if idx == 1:
            d1 = 10*math.sin(t)
            d2 = 0
        else:
            d1 = 0
            d2 = 10*math.sin(t)
        
        shared.game.screen.blit(self.title, (shared.screenSize[0]/2-self.title.get_size()[0]/2,20-dy))
        if shared.score > 0 :
            shared.game.screen.blit(self.retry,  (shared.screenSize[0]/2-self.play .get_size()[0]/2+d1,300))
        else:
            shared.game.screen.blit(self.play,  (shared.screenSize[0]/2-self.play .get_size()[0]/2+d1,300))
        shared.game.screen.blit(self.quit,  (shared.screenSize[0]/2-self.quit .get_size()[0]/2+d2,500+dy))
