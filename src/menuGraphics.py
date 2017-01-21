import pygame, math

import src.shared as shared

class MenuGraphics() :

    def __init__(self) :
        pass

    def update(self) :

        pass

    def render(self, idx, dy) :
        shared.game.screen.blit(shared.assetsdb["bottomline"], (0,0))

        t = 1000*pygame.time.get_ticks()
        if idx == 1:
            d1 = 40+2*math.sin(t)
            d2 = 0
        else:
            d1 = 0
            d2 = 40+2*math.sin(t)
        
        shared.game.screen.blit(shared.assetsdb["title"], (1280/2-400/2,20-dy))
        shared.game.screen.blit(shared.assetsdb["menu_play"], (1280/2-300/2+d1,300))
        shared.game.screen.blit(shared.assetsdb["menu_quit"], (1280/2-300/2+d2,500+dy))
