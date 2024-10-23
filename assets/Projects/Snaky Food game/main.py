import pygame
import time
import random

# Initialize the game
pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Screen dimensions
width = 600
height = 400

# Create a game window
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define the clock to control the game's speed
clock = pygame.time.Clock()

# Snake properties
snake_block = 10
snake_speed = 15

# Fonts for the score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(display, green, [block[0], block[1], snake_block, snake_block])

# Function to display game messages
def game_message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [width / 6, height / 3])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x = width / 2
    y = height / 2

    # Snake's movement coordinates
    x_change = 0
    y_change = 0

    # Snake's body
    snake_list = []
    length_of_snake = 1

    # Random food position
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(blue)
            game_message("You Lost! Press Q-Quit or C-Play Again", red)
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle events (keyboard inputs)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Update snake position
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        display.fill(black)

        # Draw food
        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])

        # Snake movement
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Check if snake has eaten the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Control the speed of the game
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
