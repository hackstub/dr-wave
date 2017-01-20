# Misc system stuff
import sys

# Pygame
import pygame
from pygame.locals import *

# Game specific
import src.shared as shared
import src.game as game
import src.background as background
import src.character as character


def main() :
    
    shared.game = game.Game()

    shared.loadAssets()
    
    shared.background = background.Background()
    shared.character  = character.Character()

    while True :

        shared.game.mainLoop()


main()
