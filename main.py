'''
Usa Python 2.7
No se pueden poner acentos ni "ny"

PARA QUE INTELLISENSE FUNCIONE CON PYGAME:
Go to your pygame folder and open init.py in a text editor
Navigate to the import section with the try/except clauses (around line 109)
Change the format from import pygame.module to from pygame import module for the modules you want
For example, change

try: import pygame.event
to

try: from pygame import event
Restart PyCharm and it should work :)
'''


#3rd party modules
import pygame
import libtcodpy

#game files
import constans


def draw_game():

    global SURFACE_MAIN

    # Rellena la Surface con un color
    SURFACE_MAIN.fill(constans.COLOR_DEFAULT_BG)

    #TODO dibujar el mapa

    # dibujar el personaje
    SURFACE_MAIN.blit(constans.S_PLAYER, (200, 200))

    # actualiza la pantalla
    pygame.display.flip()



def game_main_loop():
    ''' En esta funcion, entramos en el bucle principal del juego '''
    game_quit = False

    while not game_quit:

        # get player input
        events_lists = pygame.event.get()

        # process input
        for event in events_lists:
            if event.type == pygame.QUIT:
                game_quit = True



        # draw the game
        draw_game()

    # quit the game
    pygame.quit()
    exit()

def game_initialize():
    ''' Esta funcion inicializa la ventana principal y pygame '''

    global SURFACE_MAIN

    #inicializa pygame
    pygame.init()

    # pygame.display.set_mode retorna una Surface
    SURFACE_MAIN = pygame.display.set_mode((constans.GAME_WIDTH, constans.GAME_HEIGHT))


if __name__ == '__main__':
    game_initialize()
    game_main_loop()
