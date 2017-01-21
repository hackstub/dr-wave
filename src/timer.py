import sys, pygame, math

import src.shared as shared

class Timer() :

    def __init__(self) :
        self.t0 = pygame.time.get_ticks()

    def update(self) : self.t = pygame.time.get_ticks()

    def render(self) :
        t, dx = math.floor((self.t-self.t0)/100), 0
        for c in str(t):
            shared.game.screen.blit(shared.assetsdb[c], (24+dx, 24))
            dx += 48
