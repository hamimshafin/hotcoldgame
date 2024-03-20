import pygame
import random
import math

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

pygame.display.set_caption('Hot Cold Game')

# Set up the clock
clock = pygame.time.Clock()
fps_limit = 60

# Game data
user_pos = [SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2]
hidden_pos = [random.randint(50, SCREEN_SIZE[0] - 50), random.randint(50, SCREEN_SIZE[1] - 50)]
circle_size = 50
user_color = RED

# Function to reset hidden circle location
def set_hidden_location():
    hidden_pos[0] = random.randint(50, SCREEN_SIZE[0] - 50)
    hidden_pos[1] = random.randint(50, SCREEN_SIZE[1] - 50)

# Function to play the game
def play_game():
    global user_pos, user_color
    run_game = True

    while run_game:
        clock.tick(fps_limit)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    user_pos[0] -= 10
                elif event.key == pygame.K_RIGHT:
                    user_pos[0] += 10
                elif event.key == pygame.K_UP:
                    user_pos[1] -= 10
                elif event.key == pygame.K_DOWN:
                    user_pos[1] += 10

        # Calculate distance between user's circle and hidden circle
        distance = math.sqrt((user_pos[0] - hidden_pos[0]) ** 2 + (user_pos[1] - hidden_pos[1]) ** 2)

        # Adjust user's circle color based on distance from the hidden circle
        if distance < 50:
            user_color = GREEN
        elif distance < 100:
            user_color = RED
        else:
            user_color = BLUE

        # Fill the screen with black
        screen.fill(BLACK)

        # Draw circles
        pygame.draw.circle(screen, user_color, user_pos, circle_size)
        pygame.draw.circle(screen, WHITE, hidden_pos, circle_size)

        pygame.display.flip()

# Function to start the game
def start_game():
    set_hidden_location()
    play_game()
def set_difficulty

def display_menu():
    menu = pygame.menu.Menu('Hot/Cold Game', 400, 300, theme=pygame.menu.themes.THEME_BLUE)
    menu.add.selector('Difficulty :', [('Level 1', 1), ('Level 2', 2), ('Level 3', 3)], onchange=set_difficulty)
    menu.add.button('Play', play_game)
    menu.add.button('Quit', pygame.menu.events.EXIT)
    menu.mainloop(SCREEN)

# Main game loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    start_game()

        screen.fill(BLACK)
        pygame.display.flip()

if __name__ == '__main__':
    start_game()
    main()
