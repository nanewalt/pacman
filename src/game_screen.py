import pygame
from components.button import foo

'''
handles game screen
'''

# window constants
pygame.init()
size = width, height = 1200, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pacman')
