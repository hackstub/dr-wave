import sys, pygame, math

import src.shared as shared

class ScoreDisplay() :

    def __init__(self) :
        pass

    def update(self) : pass

    def render(self) :
        if shared.score>0:
            shared.game.screen.blit(shared.assetsdb["over"], (24, 230))
            t, dx = math.floor(shared.score/1000), 0
            for c in str(t):
                shared.game.screen.blit(shared.assetsdb["timer_digits"].sprites[int(c)], (220+dx, 450))
                dx += 48

