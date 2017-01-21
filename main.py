# Misc system stuff
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
pygame.mixer.init()

def main() :
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


main()
