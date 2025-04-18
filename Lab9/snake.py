import pygame
import random
import sys
import time
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

ASSETS = os.path.join(os.path.dirname(__file__), "assets")
eat_sound = pygame.mixer.Sound(os.path.join(ASSETS, "coin.mp3"))
crash_sound = pygame.mixer.Sound(os.path.join(ASSETS, "crash.mp3"))

snake = [(5, 5)]
direction = (1, 0)
score = 0
speed = 10
game_over = False

food_weights = [1, 2, 3]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
food_value = random.choice(food_weights)
food_timer = time.time()
FOOD_LIFETIME = 5

def draw_grid():
    win.fill(GREEN)
    pygame.draw.rect(win, RED, (food[0]*CELL_SIZE, food[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    food_text = font.render(str(food_value), True, BLACK)
    win.blit(food_text, (food[0]*CELL_SIZE + 5, food[1]*CELL_SIZE))
    for segment in snake:
        pygame.draw.rect(win, BLACK, (segment[0]*CELL_SIZE, segment[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))
    pygame.display.update()

def reset_game():
    global snake, direction, food, food_value, score, speed, game_over, food_timer
    snake = [(5, 5)]
    direction = (1, 0)
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    food_value = random.choice(food_weights)
    food_timer = time.time()
    score = 0
    speed = 10
    game_over = False

def update_snake():
    global food, food_value, score, speed, game_over, food_timer
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    if new_head[0] < 0 or new_head[0] >= GRID_WIDTH or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT:
        crash_sound.play()
        game_over = True
        return
    if new_head in snake:
        crash_sound.play()
        game_over = True
        return
    snake.insert(0, new_head)
    if new_head == food:
        eat_sound.play()
        score += food_value
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        food_value = random.choice(food_weights)
        food_timer = time.time()
        if score % 5 == 0:
            speed += 2
    else:
        snake.pop()
    if time.time() - food_timer > FOOD_LIFETIME:
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        food_value = random.choice(food_weights)
        food_timer = time.time()

while True:
    clock.tick(speed)
    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)
        update_snake()
        draw_grid()
    else:
        win.fill(BLACK)
        over_text = font.render("Game Over! Press R to Restart", True, YELLOW)
        score_text = font.render(f"Final Score: {score}", True, WHITE)
        win.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 20))
        win.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 20))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
