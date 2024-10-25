import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle and ball settings
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_RADIUS = 10
PADDLE_VELOCITY = 7
BALL_VELOCITY_X = 5
BALL_VELOCITY_Y = 5

# Paddle and ball positions
left_paddle = pygame.Rect(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)

# Score
left_score = 0
right_score = 0
WINNING_SCORE = 5

font = pygame.font.Font(None, 74)

# Game loop
running = True
while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    # Left paddle movement
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_VELOCITY
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_VELOCITY
    
    # Right paddle movement
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_VELOCITY
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_VELOCITY
    
    # Ball movement
    ball.x += BALL_VELOCITY_X
    ball.y += BALL_VELOCITY_Y
    
    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_VELOCITY_Y *= -1
    
    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_VELOCITY_X *= -1
    
    # Ball out of bounds
    if ball.left <= 0:
        right_score += 1
        ball.x = WIDTH // 2 - BALL_RADIUS
        ball.y = HEIGHT // 2 - BALL_RADIUS
        BALL_VELOCITY_X *= -1
        BALL_VELOCITY_Y *= random.choice([1, -1])
    if ball.right >= WIDTH:
        left_score += 1
        ball.x = WIDTH // 2 - BALL_RADIUS
        ball.y = HEIGHT // 2 - BALL_RADIUS
        BALL_VELOCITY_X *= -1
        BALL_VELOCITY_Y *= random.choice([1, -1])
    
    # Drawing
    WIN.fill(BLACK)
    
    pygame.draw.rect(WIN, WHITE, left_paddle)
    pygame.draw.rect(WIN, WHITE, right_paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    
    left_text = font.render(str(left_score), True, WHITE)
    WIN.blit(left_text, (WIDTH//4 - left_text.get_width()//2, 20))
    
    right_text = font.render(str(right_score), True, WHITE)
    WIN.blit(right_text, (3*WIDTH//4 - right_text.get_width()//2, 20))
    
    if left_score >= WINNING_SCORE:
        WIN.fill(BLACK)
        win_text = font.render("Left Player Wins!", True, WHITE)
        WIN.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - win_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False
    elif right_score >= WINNING_SCORE:
        WIN.fill(BLACK)
        win_text = font.render("Right Player Wins!", True, WHITE)
        WIN.blit(win_text, (WIDTH//2 - win_text.get_width()//2, HEIGHT//2 - win_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(3000)
        running = False
    
    pygame.display.update()

pygame.quit()
