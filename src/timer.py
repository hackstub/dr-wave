import sys, pygame, math

import src.shared as shared

class Timer() :

    def __init__(self) :
        self.t0 = pygame.time.get_ticks()
        
        self.box    = shared.assetsdb["timer_box"]
        self.digits = shared.assetsdb["timer_digits"]

    def update(self) :
    
        self.t = pygame.time.get_ticks()
        self.dt = self.t-self.t0

    def render(self) :
        t, dx = math.floor((self.dt)/100), 0
        shared.game.screen.blit(self.box,     (shared.screenSize[0]-188, 12))
        for c in str(t):
            shared.game.screen.blit(self.digits.sprites[int(c)],
                    (shared.screenSize[0]-24+dx-48*len(str(t)), 34))
            dx += 48
