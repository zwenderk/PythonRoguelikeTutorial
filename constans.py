import pygame

pygame.init()

#Game sizes
GAME_WIDTH = 800
GAME_HEIGHT = 600

#Color definitions
COLOR_BRACK = (0, 0, 0)
COLOR_WHIT = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

#Game colors
COLOR_DEFAULT_BG = COLOR_GREY

#Sprites: pygame.image.load retorna una Surface
S_PLAYER = pygame.image.load("data/python.png")