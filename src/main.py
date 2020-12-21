import pygame

'''
This class will handle the main menu where users can play a game, create a level, and tweak options
'''

# window setup
pygame.init()
size = width, height = 1200, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pacman')

# colors
background_color = (0, 0, 0)

'''
update the screen based on user actions
'''
def draw():
    screen.fill(background_color)
    pygame.display.update()

'''
handle user starting application
'''
if __name__ == '__main__':
    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()
