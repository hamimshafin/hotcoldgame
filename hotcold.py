import math
import sys
import pygame
import pygame.mixer
import pygame.menu
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


def play_game():
    global game

    clock = pygame.time.Clock()
    run_game = True

    while run_game:
        clock.tick(fps_limit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game['user_posx'] -= 10
                elif event.key == pygame.K_RIGHT:
                    game['user_posx'] += 10
                elif event.key == pygame.K_UP:
                    game['user_posy'] -= 10
                elif event.key == pygame.K_DOWN:
                    game['user_posy'] += 10
                elif event.key == pygame.K_r:
                    # Reset hidden circle location
                    set_hidden_location()
                    # Reset user circle color
                    game['user_circle_color'] = blue

        # Calculate the distance between the user's circle and the hidden circle
        distance = math.sqrt((game['user_posx'] - game['hidden_posx']) ** 2 + (game['user_posy'] - game['hidden_posy']) ** 2)

        # Adjust user's circle color based on distance from the hidden circle
        if distance < 100:
            game['user_circle_color'] = red
        elif distance < game['circle_size']:
            game['user_circle_color'] = green
        else:
            game['user_circle_color'] = blue

        # Fill the screen with black
        screen.fill(black)

        # Draw circles
        pygame.draw.circle(screen, game['user_circle_color'], (game['user_posx'], game['user_posy']), game['circle_size'])
        pygame.draw.circle(screen, game['hidden_circle_color'], (game['hidden_posx'], game['hidden_posy']), game['circle_size'])

        pygame.display.flip()








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
    global game
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


def display_instructions():
    font = pygame.font.SysFont(None, 24)

    line = font.render('# ' + str(game['num_moves']) + "moves", True, YELLOW)
    SCREEN.blit(line, (20, 20))

    # display debug mode
    debug_text = font.render('Debug: d', True, YELLOW)
    SCREEN.blit(debug_text, (20, 40))

    # Display reset instruction
    reset_text = font.render('Reset : r', True, YELLOW)
    SCREEN.blit(reset_text, 20, 60)


def set_difficulty(level, difficulty):
    global game

    if difficulty == 3:
        game['circle_size'], game['move_size'] = (10, 10)
    elif difficulty == 2:
        game['circle_size'], game['move_size'] = (25, 25)
    else:
        game['circle_size'], game['move_size'] = (50, 50)


def display_menu():
    menu = pygame.menu.Menu('Hot/Cold Game', 400, 300, theme=pygame.menu.themes.THEME_BLUE)
    menu.add.selector('Difficulty :', [('Level 1', 1), ('Level 2', 2), ('Level 3', 3)], onchange=set_difficulty)
    menu.add.button('Play', play_game)  # call play_game function
    menu.add.button('Quit', pygame.menu.events.EXIT)
    menu.mainloop(SCREEN)


def main():
    pygame.init()
    pygame.display.set_caption('Hot Cold Game')

    display_menu()
    pygame.quit()



if __name__ == "__main__":
    main()
