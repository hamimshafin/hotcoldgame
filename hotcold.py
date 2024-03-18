import math
import sys
import pygame
import pygame_menu
import random

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
pygame.display.set_caption('Hot Cold Game')

# Define game data
game = {
    'circle_size': 50,
    'move_size': 50,
    'user_posx': SCREEN_SIZE // 2,
    'user_posy': SCREEN_SIZE // 2,
    'hidden_posx': 0,
    'hidden_posy': 0,
    'user_circle_color': WHITE,
    'hidden_circle_color': BLACK,
    'num_moves': 0
}

# Function to play the game
def play_game():
    clock = pygame.time.Clock()
    run_game = True

    while run_game:
        clock.tick(60)

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
                    set_hidden_location()
                    game['user_circle_color'] = BLUE

        distance = math.sqrt((game['user_posx'] - game['hidden_posx']) ** 2 +
                             (game['user_posy'] - game['hidden_posy']) ** 2)

        if distance < 100:
            game['user_circle_color'] = RED
        elif distance < game['circle_size']:
            game['user_circle_color'] = GREEN
        else:
            game['user_circle_color'] = BLUE

        SCREEN.fill(BLACK)
        pygame.draw.circle(SCREEN, game['user_circle_color'], (game['user_posx'], game['user_posy']), game['circle_size'])
        pygame.draw.circle(SCREEN, game['hidden_circle_color'], (game['hidden_posx'], game['hidden_posy']), game['circle_size'])

        pygame.display.flip()

# Function to set the hidden circle location
def set_hidden_location():
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
    menu = pygame.menu.Menu('Hot/Cold Game', 400, 300, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Difficulty :', [('Level 1', 1), ('Level 2', 2), ('Level 3', 3)], onchange=set_difficulty)
    menu.add.button('Play', play_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SCREEN)


# Main function
def main():
    pygame.init()
    display_menu()
    pygame.quit()

if __name__ == "__main__":
    main()
