import os, sys, math, pygame, pygame.mixer
from pygame.locals import *
import random

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

screen_size = screen_width, screen_height = 600, 400
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Hot Cold Game')

fps_limit = 60

# circle
user_colorcircle = (red)
user_posx = 300
user_posy = 200
circle = pygame.draw.circle(screen, user_colorcircle, (user_posx, user_posy), 50)

# Hidden circle
hidden_colorcircle = white
hidden_posx = 500
hidden_posy = 100


def play_game():
    global user_posy, user_posx

    clock = pygame.time.Clock()

    run_me = True

    while run_me:
        clock.tick(fps_limit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_me = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    user_posx -= 10

                if event.key == pygame.K_RIGHT:
                    user_posx += 10

                if event.key == pygame.K_UP:
                    user_posy -= 10

                if event.key == pygame.K_DOWN:
                    user_posy += 10

                if event.key == pygame.K_r:
                    # Reset hidden circle location
                    set_hidden_location()

        # fill the screen with black (otherwise, the circle will leave a trail)
        screen.fill(black)
        # redraw the circle
        pygame.draw.circle(screen, user_colorcircle, (user_posx, user_posy), 50)
        pygame.draw.circle(screen, hidden_colorcircle, (hidden_posx, hidden_posy), 50)
        pygame.display.flip()


# game data that never changes

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 233, 0)

SCREEN_SIZE = 800
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
# game data that can change values

game = {
    'circle_size': 50,
    'move size': 50,
    'prev_x': 0,
    'prev_y': 0,
    'user_x': SCREEN_SIZE / 2,
    'user_y': SCREEN_SIZE / 2,
    'hidden_x': 0,
    'hidden_y': 0,
    'user_color': WHITE,
    'hidden_color': BLACK,
    'num_moves': 0
}


def set_hidden_location():
    global game

    user_pos = SCREEN_SIZE / 2  # center of the screen

    inside_dist = game['circle_size']
    outside_dist = SCREEN_SIZE - game['circle_size']

    right_user_dist = user_pos - game['circle_size']  # at least one circle away on the right
    left_user_dist = user_pos + game['circle_size']  # at least one circle away on the left

    # keep looping until a valid location is generated within the screen size and not touching the user's circle

    while True:
        # hidden location not in center where the user's circle is & yet still inside the screen
        x = random.randint(inside_dist, outside_dist)
        y = random.randint(inside_dist, outside_dist)

        # make sure the hidden circle is not near the user's circle

        if (x < right_user_dist or x > left_user_dist) and (y < right_user_dist or y > left_user_dist):
            game['hidden_x'] = x
            game['hidden_y'] = y
            return


def debug():
    # initialising pygame
    pygame.init()

    # creating a running loop
    while True:

        # creating a loop to check events that
        # are occurring
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:
                # if keydown event happened
                if event.key == pygame.K_r:
                    set_hidden_location()
                # than printing a string to output
                print("Hidden circle location reset")
                print("A key has been pressed")


def main():
    pygame.init()
    pygame.display.set_caption('Hot Cold Game')

    play_game()
    debug()
    pygame.quit()


if __name__ == "__main__":
    main()
