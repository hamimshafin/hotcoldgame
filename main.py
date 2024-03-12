import pygame
import random
from pygame.locals import *

# global variables used to control the game
s = None           # used to configure the screen
t = None           # pen used to draw the circles and text on the screen
num_moves = 0      # running total of the number of moves to find the hidden circle
circle_size = 100  # set the difficulty of the game by the size of the circles
move_size = 100    # set the difficulty of the game by the size of the circles

# previous location of the user's circle used to determine if the user is getting closer or further away
previous_x = 0
previous_y = 0


# current location of the user's circle
x = 0  # start at the center of screen and used to move right (+) or left (-)
y = 0  # start at the center of screen and used to move up (+) or down (-)

# used to control the hidden circle location
hidden_x = 0  # from the center of the screen right (+) left (-)
hidden_y = 0  # from the center of the screen up (+) down (-)

user_color = 'blue'     # the color of the user's circle: (closer) cold=blue, (further) hot=red
hidden_color = 'black'  # the default for the hidden circle is black to match the screen background color

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
WHITE = (255,255,255)
YELLOW = (255, 233, 0)


SCREEN_SIZE = 800
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

clock = pygame.time.Clock()
fps_limit = 60

#circle
user_color = (WHITE)
hidden_color = (BLACK)

user_posx = 300
user_posy = 200

hidden_posx = 100
hidden_posy = 100


#game data that can change values

game = {
    'circle_size': 50,
    'move size': 50,
    'prev_x': 0,
    'prev_y': 0,
    'user_x': SCREEN_SIZE / 2,
    'user_y': SCREEN_SIZE/2,
    'hidden_x': 0,
    'hidden_y': 0,
    'user_color': WHITE,
    'hidden_color': BLACK,
    'num_moves': 0
}

def play_game():
    """..."""
    global game

    while True:
        clock.tick(fps_limit)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_me = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pos_x -= 10

                if event.key == pygame.K_RIGHT:
                    posx += 10

                if event.key == pygame.K_UP:
                    posy += 10

                if event.key == pygame.K_DOWN:
                    posy -=10

