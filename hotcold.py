import pygame
import pygame_menu
import random
import pygame.mixer

'''
 scripted level docstring (https://github.com/hamimshafin/hotcoldgame)
 imports random, pygame, pygame_menu
dunders (metadata) for the authorship information (example):
__author__ = 'Hamim Shafin'
__version__ = '1.0'
__date__ = '2024.03.18'
__status__ = 'Development'
 global variables
 functions arrange in a logical order based on usage
 main function
 if __name__ = "main"
'''

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 233, 0)

# Define screen size
SCREEN_SIZE = 800
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

# Define game data
game = {
    'circle_size': 50,
    'move_size': 50,
    'user_posx': SCREEN_SIZE // 2,
    'user_posy': SCREEN_SIZE // 2,
    'hidden_posx': 0,
    'hidden_posy': 0,
    'previous_x': SCREEN_SIZE // 2,  # Initialize with starting position
    'previous_y': SCREEN_SIZE // 2,  # Initialize with starting position
    'user_color': WHITE,
    'hidden_color': BLACK,
    'num_moves': 0,
}


# Function to play the game
def play_game():
    global game
    clock = pygame.time.Clock()
    run_game = True

    while run_game:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame.KEYDOWN:
                game['previous_x'] = game['user_posx']
                game['previous_y'] = game['user_posy']
                if event.key == pygame.K_LEFT:
                    game['user_posx'] -= 20
                    game['num_moves'] += 1  # Increment move counter
                elif event.key == pygame.K_RIGHT:
                    game['user_posx'] += 20
                    game['num_moves'] += 1  # Increment move counter
                elif event.key == pygame.K_UP:
                    game['user_posy'] -= 20
                    game['num_moves'] += 1  # Increment move counter
                elif event.key == pygame.K_DOWN:
                    game['user_posy'] += 20
                    game['num_moves'] += 1  # Increment move counter
                elif event.key == pygame.K_r:
                    reset_game()
                elif event.key == pygame.K_d:
                    debug_mode_toggle()

        set_circle_colors()

        SCREEN.fill(BLACK)
        pygame.draw.circle(SCREEN, game['user_color'], (game['user_posx'], game['user_posy']),
                           game['circle_size'])

        pygame.draw.circle(SCREEN, game['hidden_color'], (game['hidden_posx'], game['hidden_posy']), game['circle_size'])

        # Display Instructions
        display_instructions()

        pygame.display.flip()


# Function to set_circle colors
def set_circle_colors():
    global game
    overlap = game['circle_size'] * 2 - 10

    if abs(game['user_posx'] - game['hidden_posx']) < overlap and abs(
            game['user_posy'] - game['hidden_posy']) < overlap:
        game['hidden_color'] = YELLOW
        game['user_color'] = GREEN

    else:
        if game['previous_x'] != game['user_posx']:
            if abs(game['previous_x'] - game['hidden_posx']) > abs(game['user_posx'] - game['hidden_posx']):
                game['user_color'] = RED
            else:
                game['user_color'] = BLUE

        if game['previous_y'] != game['user_posy']:
            if abs(game['previous_y'] - game['hidden_posy']) > abs(game['user_posy'] - game['hidden_posy']):
                game['user_color'] = RED
            else:
                game['user_color'] = BLUE


game['previous_x'] = game['user_posx']
game['previous_x'] = game['user_posy']


# Function to set the hidden circle location
def set_hidden_location():
    global game
    inside_dist = game['circle_size']
    outside_dist = SCREEN_SIZE - game['circle_size']

    right_user_dist = game['user_posx'] - game['circle_size']
    left_user_dist = game['user_posx'] + game['circle_size']

    while True:
        x = random.randint(inside_dist, outside_dist)
        y = random.randint(inside_dist, outside_dist)

        if (x < right_user_dist or x > left_user_dist) and (y < right_user_dist or y > left_user_dist):
            game['hidden_posx'] = x
            game['hidden_posy'] = y
            return


def reset_game():
    global game
    game['num_moves'] = 0
    game['user_color'] = WHITE
    game['user_posx'] = SCREEN_SIZE // 2
    game['user_posy'] = SCREEN_SIZE // 2
    set_hidden_location()
    game['user_color'] = BLUE


def debug_mode_toggle():
    global game

    if game['hidden_color'] == BLACK:
        game['hidden_color'] = WHITE
    else:
        game['hidden_color'] = BLACK

    play_game()


# Function to display instructions
def display_instructions():
    font = pygame.font.SysFont(None, 24)
    line = font.render('# ' + str(game['num_moves']) + "moves", True, YELLOW)
    SCREEN.blit(line, (20, 20))
    debug_text = font.render('Debug: d', True, YELLOW)
    SCREEN.blit(debug_text, (20, 40))
    reset_text = font.render('Reset : r', True, YELLOW)
    SCREEN.blit(reset_text, (20, 60))


# Function to set difficulty level
def set_difficulty(level, difficulty):
    if difficulty == 3:
        game['circle_size'], game['move_size'] = (10, 10)
    elif difficulty == 2:
        game['circle_size'], game['move_size'] = (25, 25)
    else:
        game['circle_size'], game['move_size'] = (50, 50)


# Function to display the menu
def display_menu():
    menu = pygame_menu.Menu('Hot/Cold Game', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Difficulty :', [('Level 1', 1), ('Level 2', 2), ('Level 3', 3)], onchange=set_difficulty)
    menu.add.button('Play', play_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SCREEN)


# Function to play music
def play_music():
    pygame.mixer.init()
    pygame.mixer_music.load('Meet & Fun! - Ofshane.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)


# Main function
def main():
    play_music()
    pygame.display.set_caption('Hot Cold Game')
    pygame.init()
    display_menu()
    pygame.quit()


if __name__ == "__main__":
    main()
