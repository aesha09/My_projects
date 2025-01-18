# Import required modules
import random
import sys
import pygame
from pygame.locals import *

# Game Constants
WINDOW_WIDTH = 288
WINDOW_HEIGHT = 512
FPS = 30

# Asset paths (update these paths as per your local directory structure)
BACKGROUND_IMAGE = 'sprites\\background-day.png'
BIRD_IMAGE = 'sprites\\bluebird-midflap.png'
PIPE_IMAGE = 'sprites\\pipe-green.png'
BASE_IMAGE = 'sprites\\base.png'
SCORE_IMAGES = ['sprites/{}.png'.format(i) for i in range(10)]

# Initialize Pygame
pygame.init()
FPSCLOCK = pygame.time.Clock()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Load game assets
GAME_SPRITES = {
    'background': pygame.image.load(BACKGROUND_IMAGE).convert(),
    'bird': pygame.image.load(BIRD_IMAGE).convert_alpha(),
    'pipe': (
        pygame.transform.rotate(pygame.image.load(PIPE_IMAGE).convert_alpha(), 180),
        pygame.image.load(PIPE_IMAGE).convert_alpha()
    ),
    'base': pygame.image.load(BASE_IMAGE).convert_alpha(),
    'numbers': [pygame.image.load(img).convert_alpha() for img in SCORE_IMAGES]
}

# Other game variables
GROUND_Y = WINDOW_HEIGHT * 0.8


def main():
    """Main function to run the game."""
    while True:
        # Start screen
        welcome_screen()
        # Main game loop
        main_game()


def welcome_screen():
    """Display the welcome screen."""
    bird_x = int(WINDOW_WIDTH / 5)
    bird_y = int(WINDOW_HEIGHT / 2)
    base_x = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
        # Blit assets
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        SCREEN.blit(GAME_SPRITES['bird'], (bird_x, bird_y))
        SCREEN.blit(GAME_SPRITES['base'], (base_x, GROUND_Y))
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def main_game():
    """Main game logic."""
    score = 0
    bird_x = int(WINDOW_WIDTH / 5)
    bird_y = int(WINDOW_HEIGHT / 2)
    base_x = 0

    # Generate two pipes
    pipes = [create_pipe(), create_pipe()]

    # Adjust pipes for the starting positions
    pipes[1]['x'] += WINDOW_WIDTH / 2

    # Bird and pipe movement
    bird_velocity_y = -9
    bird_flapped = False
    pipe_velocity_x = -4

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                bird_velocity_y = -9
                bird_flapped = True

        # Check for collision
        if check_collision(bird_x, bird_y, pipes):
            return

        # Update score
        bird_mid_pos = bird_x + GAME_SPRITES['bird'].get_width() / 2
        for pipe in pipes:
            pipe_mid_pos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width() / 2
            if pipe_mid_pos <= bird_mid_pos < pipe_mid_pos + 4:
                score += 1

        # Bird movement
        if bird_velocity_y < 10 and not bird_flapped:
            bird_velocity_y += 1
        bird_y += min(bird_velocity_y, GROUND_Y - bird_y - GAME_SPRITES['bird'].get_height())
        bird_flapped = False

        # Pipe movement
        for pipe in pipes:
            pipe['x'] += pipe_velocity_x

        # Add new pipe and remove old ones
        if pipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            pipes.pop(0)
            pipes.append(create_pipe())

        # Render the game
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for pipe in pipes:
            SCREEN.blit(GAME_SPRITES['pipe'][0], (pipe['x'], pipe['upper_y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1], (pipe['x'], pipe['lower_y']))
        SCREEN.blit(GAME_SPRITES['base'], (base_x, GROUND_Y))
        SCREEN.blit(GAME_SPRITES['bird'], (bird_x, bird_y))
        display_score(score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def create_pipe():
    """Generate positions for a new pipe."""
    pipe_height = GAME_SPRITES['pipe'][0].get_height()
    offset = WINDOW_HEIGHT / 3
    lower_y = random.randint(int(WINDOW_HEIGHT / 2), int(WINDOW_HEIGHT - offset))
    upper_y = lower_y - offset - pipe_height
    return {'x': WINDOW_WIDTH + 10, 'upper_y': upper_y, 'lower_y': lower_y}


def check_collision(bird_x, bird_y, pipes):
    """Check if the bird has collided with pipes or ground."""
    if bird_y > GROUND_Y - 25 or bird_y < 0:
        return True

    bird_rect = pygame.Rect(bird_x, bird_y, GAME_SPRITES['bird'].get_width(), GAME_SPRITES['bird'].get_height())
    for pipe in pipes:
        upper_rect = pygame.Rect(pipe['x'], pipe['upper_y'], GAME_SPRITES['pipe'][0].get_width(), GAME_SPRITES['pipe'][0].get_height())
        lower_rect = pygame.Rect(pipe['x'], pipe['lower_y'], GAME_SPRITES['pipe'][1].get_width(), GAME_SPRITES['pipe'][1].get_height())
        if bird_rect.colliderect(upper_rect) or bird_rect.colliderect(lower_rect):
            return True
    return False


def display_score(score):
    """Display the current score on the screen."""
    score_digits = [int(x) for x in str(score)]
    total_width = sum(GAME_SPRITES['numbers'][digit].get_width() for digit in score_digits)
    x_offset = (WINDOW_WIDTH - total_width) / 2

    for digit in score_digits:
        SCREEN.blit(GAME_SPRITES['numbers'][digit], (x_offset, WINDOW_HEIGHT * 0.1))
        x_offset += GAME_SPRITES['numbers'][digit].get_width()


if __name__ == "__main__":
    main()
