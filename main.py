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



#      _______.___________..______       __    __    ______ .___________.
#     /       |           ||   _  \     |  |  |  |  /      ||           |
#    |   (----`---|  |----`|  |_)  |    |  |  |  | |  ,----'`---|  |----`
#     \   \       |  |     |      /     |  |  |  | |  |         |  |
# .----)   |      |  |     |  |\  \----.|  `--'  | |  `----.    |  |
# |_______/       |__|     | _| `._____| \______/   \______|    |__|

class struct_Tile:
    def __init__(self, block_path):
        self.block_path = block_path



#   ______   .______          __   _______   ______ .___________.    _______.
#  /  __  \  |   _  \        |  | |   ____| /      ||           |   /       |
# |  |  |  | |  |_)  |       |  | |  |__   |  ,----'`---|  |----`  |   (----`
# |  |  |  | |   _  <  .--.  |  | |   __|  |  |         |  |        \   \
# |  `--'  | |  |_)  | |  `--'  | |  |____ |  `----.    |  |    .----)   |
#  \______/  |______/   \______/  |_______| \______|    |__|    |_______/

class obj_Actor:
    def __init__(self, x, y, sprite):
        self.x = x  # Direccion en el mapa
        self.y = y  # Direccion en el mapa
        self.sprite = sprite

    def draw(self):
        SURFACE_MAIN.blit(self.sprite, (self.x * constans.CELL_WIDTH, self.y * constans.CELL_HEIGHT))

    def move(self, dx, dy):
        if GAME_MAP[self.x + dx][self.y + dy].block_path == False:
            self.x += dx
            self.y += dy





# .___  ___.      ___      .______
# |   \/   |     /   \     |   _  \
# |  \  /  |    /  ^  \    |  |_)  |
# |  |\/|  |   /  /_\  \   |   ___/
# |  |  |  |  /  _____  \  |  |
# |__|  |__| /__/     \__\ | _|

def map_create():
    new_map = [[struct_Tile(False) for y in range(0, constans.MAP_HEIGHT)] for x in range(0, constans.MAP_WIDTH)] # Crea mapa vacio con una lista comprimida

    new_map[10][10].block_path = True # Asigna a la variable block_path del objeto que esta en [10][10] en valor True
    new_map[10][15].block_path = True

    return new_map


#  _______  .______          ___   ____    __    ____  __  .__   __.   _______
# |       \ |   _  \        /   \  \   \  /  \  /   / |  | |  \ |  |  /  _____|
# |  .--.  ||  |_)  |      /  ^  \  \   \/    \/   /  |  | |   \|  | |  |  __
# |  |  |  ||      /      /  /_\  \  \            /   |  | |  . `  | |  | |_ |
# |  '--'  ||  |\  \----./  _____  \  \    /\    /    |  | |  |\   | |  |__| |
# |_______/ | _| `._____/__/     \__\  \__/  \__/     |__| |__| \__|  \______|

def draw_game():

    global SURFACE_MAIN

    # Rellena la Surface con un color
    SURFACE_MAIN.fill(constans.COLOR_DEFAULT_BG)

    # dibujar el mapa
    draw_map(GAME_MAP)

    # dibujar el personaje
    PLAYER.draw()

    # actualiza la pantalla
    pygame.display.flip()



def draw_map(map_to_draw):
    for x in range(0, constans.MAP_WIDTH):
        for y in range(0, constans.MAP_HEIGHT):
            if map_to_draw[x][y].block_path == True:
                # Dibuja muro
                SURFACE_MAIN.blit(constans.S_WALL, (x * constans.CELL_WIDTH, y * constans.CELL_HEIGHT))
            else:
                # Dibuja suelo
                SURFACE_MAIN.blit(constans.S_FLOOR, (x * constans.CELL_WIDTH, y * constans.CELL_HEIGHT))




#   _______      ___      .___  ___.  _______
#  /  _____|    /   \     |   \/   | |   ____|
# |  |  __     /  ^  \    |  \  /  | |  |__
# |  | |_ |   /  /_\  \   |  |\/|  | |   __|
# |  |__| |  /  _____  \  |  |  |  | |  |____
#  \______| /__/     \__\ |__|  |__| |_______|

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    PLAYER.move(0, -1)
                if event.key == pygame.K_DOWN:
                    PLAYER.move(0,  1)
                if event.key == pygame.K_LEFT:
                    PLAYER.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    PLAYER.move(1,  0)





        # draw the game
        draw_game()

    # quit the game
    pygame.quit()
    exit()

def game_initialize():
    ''' Esta funcion inicializa la ventana principal y pygame '''

    global SURFACE_MAIN, GAME_MAP, PLAYER

    #inicializa pygame
    pygame.init()

    # pygame.display.set_mode retorna una Surface
    SURFACE_MAIN = pygame.display.set_mode((constans.GAME_WIDTH, constans.GAME_HEIGHT))

    GAME_MAP = map_create()

    PLAYER = obj_Actor(0, 0, constans.S_PLAYER)

#############################################################
###################################################   #######
###############################################   /~\   #####
############################################   _- `~~~', ####
##########################################  _-~       )  ####
#######################################  _-~          |  ####
####################################  _-~            ;  #####
##########################  __---___-~              |   #####
#######################   _~   ,,                  ;  `,,  ##
#####################  _-~    ;'                  |  ,'  ; ##
###################  _~      '                    `~'   ; ###
############   __---;                                 ,' ####
########   __~~  ___                                ,' ######
#####  _-~~   -~~ _                               ,' ########
##### `-_         _                              ; ##########
#######  ~~----~~~   ;                          ; ###########
#########  /          ;                        ; ############
#######  /             ;                      ; #############
#####  /                `                    ; ##############
###  /                                      ; ###############
#                                            ################

if __name__ == '__main__':
    game_initialize()
    game_main_loop()
