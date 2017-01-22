# Misc system stuff
import os
import sys

# Pygame
import pygame
from pygame.locals import *

# Game specific
import src.shared as shared
import src.menu as menu
import src.game as game
import src.menuGraphics as menuGraphics
import src.background as background
import src.character as character
import src.obstacles as obstacles

pygame.init()
pygame.mixer.init(48000)
pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])

# Fix for when game is launched with wrong cwd
if (sys.argv[0].startswith('/')) :
    os.chdir(os.path.dirname(sys.argv[0]))

def main() :
    shared.score = 0
    hsfile = open("highscore.txt", "r+")
    hs = hsfile.read()
    hsfile.close()
    shared.highscore = int(hs.strip())

    shared.game = menu.Menu()

    shared.loadAssets()
    
    shared.menuGraphics = menuGraphics.MenuGraphics()
    shared.background = background.Background()
    shared.character  = character.Character()
    shared.obstacles  = obstacles.Obstacles()

    while True :

        shared.game.mainLoop()
        
        nextScene = shared.game.getNextScene()
        
        if nextScene == "game": shared.game = game.Game()
        elif nextScene == "menu": shared.game = menu.Menu()


main()
