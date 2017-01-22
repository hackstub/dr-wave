import sys, pygame, math

import src.shared as shared

class ScoreDisplay() :

    def __init__(self) :
        pass

    def update(self) : 
        if shared.score > shared.highscore:
            shared.highscore = shared.score

    def render(self) :
        if shared.score > 0:
            shared.game.screen.blit(shared.assetsdb["over"], (24, 230))
            t, s, dx = math.floor(shared.score/1000), math.floor(shared.highscore/100), 0
            for c in str(t):
                shared.game.screen.blit(shared.assetsdb["timer_digits"].sprites[int(c)], (220+dx, 450))
                dx += 48
            dx = 0
            shared.game.screen.blit(shared.assetsdb["star"], (220, 500))
            for c in str(s):
                shared.game.screen.blit(shared.assetsdb["timer_digits"].sprites[int(c)], (220+dx, 500))
                dx += 48
            shared.game.screen.blit(shared.assetsdb["star"], (220+dx, 500))

