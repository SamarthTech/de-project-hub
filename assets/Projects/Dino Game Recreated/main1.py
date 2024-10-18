import pygame
import random
from sys import exit

pygame.init()
clock = pygame.time.Clock()

# Window dimensions
window_width = 800
window_height = 300

# Screen setup
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Doggo Run')      

# Load images
doggo_image = pygame.image.load("doggo.jpg")
cone_image = pygame.image.load("cone.png")

# Font for displaying score
font = pygame.font.Font(None, 36)  # Default font, size 36

# Rectangles for doggo and cones
doggo_rect = doggo_image.get_rect(topleft=(50, 250))  # Start position for the doggo
cone_rect = cone_image.get_rect(midbottom=(random.randint(800, 1200), 300))  # Random start for cone

# Jump control variables
is_jumping = False
ascending = False
doggo_pos_y = 250
gravity = 5

# Game speed and score
game_speed = 15
score = 0  # Initial score

# Function to handle jump
def handle_jump():
    global doggo_pos_y, is_jumping, ascending

    if is_jumping:
        if ascending:
            doggo_pos_y -= gravity  # Move up
            if doggo_pos_y <= 150:  # Max jump height
                ascending = False
        else:
            doggo_pos_y += gravity  # Move down
            if doggo_pos_y >= 250:  # Back to the ground
                doggo_pos_y = 250
                is_jumping = False  # Stop jumping

# Function to handle obstacle (cone) movement with random re-positioning
def move_cone():
    global cone_rect, score
    cone_rect.x -= game_speed
    if cone_rect.right <= 0:  # When cone goes off the screen, reset its position randomly
        cone_rect.left = random.randint(800, 1200)
        score += 1  # Increase score when the cone passes the doggo

# Function to check for collision
def check_collision():
    if doggo_rect.colliderect(cone_rect):
        return True
    return False

# Function to display score
def display_score():
    score_text = font.render(f"Score: {score}", True, (255,255,255))  # Render score text
    screen.blit(score_text, (10, 10))  # Draw score text at top-left corner

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Detect jumping
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not is_jumping:
                is_jumping = True
                ascending = True

    # Handle jump
    handle_jump()

    # Move cone (obstacle)
    move_cone()

    # Update doggo's rect position for collision detection
    doggo_rect.y = doggo_pos_y

    # Check for collision
    if check_collision():
        print("Game Over! Final Score:", score)
        pygame.quit()
        exit()

    # Drawing the game
    screen.fill((0,0,0))  # White background
    screen.blit(doggo_image, doggo_rect)  # Draw the doggo
    screen.blit(cone_image, cone_rect)  # Draw the cone
    
    # Display the score
    display_score()

    pygame.display.update()

    # Control game frame rate
    clock.tick(60)
