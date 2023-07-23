import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)

# Paddle properties
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 6

# Ball properties
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Function to draw the paddles
def draw_paddle(paddle):
    pygame.draw.rect(screen, WHITE, paddle)

# Function to draw the ball
def draw_ball(ball):
    pygame.draw.circle(screen, WHITE, (ball.x, ball.y), BALL_SIZE // 2)

# Function to update the ball's position
def move_ball(ball, ball_speed_x, ball_speed_y):
    ball.x += ball_speed_x
    ball.y += ball_speed_y

# Function to handle collisions with the top and bottom walls
def handle_wall_collision(ball, ball_speed_y):
    if ball.y <= 0 or ball.y >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    return ball_speed_y

# Function to check for collisions with the paddles
def handle_paddle_collision(ball, paddle_left, paddle_right, ball_speed_x):
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_speed_x *= -1
    return ball_speed_x

# Function to reset the ball to the center
def reset_ball(ball):
    ball.x = SCREEN_WIDTH // 2
    ball.y = SCREEN_HEIGHT // 2

# Main game loop
def main():
    paddle_left = pygame.Rect(50, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_right = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

    ball_speed_x = BALL_SPEED_X * random.choice((1, -1))
    ball_speed_y = BALL_SPEED_Y * random.choice((1, -1))

    score_left = 0
    score_right = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        # Move paddles
        if keys[pygame.K_w] and paddle_left.top > 0:
            paddle_left.y -= PADDLE_SPEED
        if keys[pygame.K_s] and paddle_left.bottom < SCREEN_HEIGHT:
            paddle_left.y += PADDLE_SPEED
        if keys[pygame.K_UP] and paddle_right.top > 0:
            paddle_right.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and paddle_right.bottom < SCREEN_HEIGHT:
            paddle_right.y += PADDLE_SPEED

        # Move the ball
        move_ball(ball, ball_speed_x, ball_speed_y)

        # Handle collisions
        ball_speed_y = handle_wall_collision(ball, ball_speed_y)
        ball_speed_x = handle_paddle_collision(ball, paddle_left, paddle_right, ball_speed_x)

        # Check for score
        if ball.x <= 0:
            score_right += 1
            reset_ball(ball)
            ball_speed_x *= -1
        elif ball.x >= SCREEN_WIDTH:
            score_left += 1
            reset_ball(ball)
            ball_speed_x *= -1

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw paddles and ball
        draw_paddle(paddle_left)
        draw_paddle(paddle_right)
        draw_ball(ball)

        # Draw score
        font = pygame.font.SysFont(None, 50)
        score_display = font.render(f"{score_left} - {score_right}", True, WHITE)
        screen.blit(score_display, (SCREEN_WIDTH // 2 - score_display.get_width() // 2, 20))

        # Update the display
        pygame.display.flip()

        # Set the frames per second
        clock.tick(60)

if __name__ == "__main__":
    main()
