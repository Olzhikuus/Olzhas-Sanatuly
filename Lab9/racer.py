import pygame
import random
import sys
import os

pygame.init()
pygame.mixer.init()

ASSETS = os.path.join(os.path.dirname(__file__), "assets")

WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

FPS = 60
clock = pygame.time.Clock()

player_img = pygame.image.load(os.path.join(ASSETS, "player_car.png"))
enemy_img = pygame.image.load(os.path.join(ASSETS, "enemy_car.png"))
coin_img = pygame.image.load(os.path.join(ASSETS, "coin.png"))
road_img = pygame.image.load(os.path.join(ASSETS, "road.png"))

player_img = pygame.transform.scale(player_img, (60, 100))
enemy_img = pygame.transform.scale(enemy_img, (60, 100))
coin_img = pygame.transform.scale(coin_img, (40, 40))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

crash_sound = pygame.mixer.Sound(os.path.join(ASSETS, "crash.mp3"))
coin_sound = pygame.mixer.Sound(os.path.join(ASSETS, "coin.mp3"))
drive_sound = pygame.mixer.Sound(os.path.join(ASSETS, "drive.mp3"))
drive_sound.play(-1)

lanes = [60, 170, 280]
player_x = lanes[1]
player_y = HEIGHT - 120
player_speed = 5

collected_coins = 0
font = pygame.font.SysFont("Arial", 24)
game_over = False

coin = {"x": random.choice(lanes), "y": -50}
coin_weights = [1, 2, 3]
coin_value = random.choice(coin_weights)
coin_speed = 4

enemy_speed = 5
speed_increase_threshold = 5
enemies = [{"x": random.choice(lanes), "y": random.randint(-600, -100)} for _ in range(2)]

def draw_window():
    win.blit(road_img, (0, 0))
    win.blit(player_img, (player_x, player_y))
    for enemy in enemies:
        win.blit(enemy_img, (enemy["x"], enemy["y"]))
    win.blit(coin_img, (coin["x"], coin["y"]))
    coin_value_text = font.render(str(coin_value), True, (0, 0, 0))
    win.blit(coin_value_text, (coin["x"] + 12, coin["y"] - 20))
    coin_text = font.render(f"Coins: {collected_coins}", True, (255, 255, 255))
    win.blit(coin_text, (WIDTH - coin_text.get_width() - 10, 10))
    pygame.display.update()

def reset_game():
    global player_x, collected_coins, enemies, coin, game_over, enemy_speed, coin_value
    player_x = lanes[1]
    collected_coins = 0
    enemy_speed = 5
    enemies = [{"x": random.choice(lanes), "y": random.randint(-600, -100)} for _ in range(2)]
    coin = {"x": random.choice(lanes), "y": -50}
    coin_value = random.choice(coin_weights)
    game_over = False
    drive_sound.play(-1)

while True:
    clock.tick(FPS)

    if not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            index = lanes.index(player_x)
            if index > 0:
                player_x = lanes[index - 1]
                pygame.time.delay(100)
        if keys[pygame.K_RIGHT]:
            index = lanes.index(player_x)
            if index < len(lanes) - 1:
                player_x = lanes[index + 1]
                pygame.time.delay(100)

        for enemy in enemies:
            enemy["y"] += enemy_speed
            if enemy["y"] > HEIGHT:
                enemy["x"] = random.choice(lanes)
                enemy["y"] = random.randint(-600, -100)

            player_rect = pygame.Rect(player_x, player_y, 60, 100)
            enemy_rect = pygame.Rect(enemy["x"], enemy["y"], 60, 100)
            if player_rect.colliderect(enemy_rect):
                crash_sound.play()
                drive_sound.stop()
                game_over = True

        coin["y"] += coin_speed
        if coin["y"] > HEIGHT:
            coin["y"] = -50
            coin["x"] = random.choice(lanes)
            coin_value = random.choice(coin_weights)

        coin_rect = pygame.Rect(coin["x"], coin["y"], 40, 40)
        player_rect = pygame.Rect(player_x, player_y, 60, 100)
        if player_rect.colliderect(coin_rect):
            collected_coins += coin_value
            coin_sound.play()
            coin["y"] = -50
            coin["x"] = random.choice(lanes)
            coin_value = random.choice(coin_weights)
            if collected_coins % speed_increase_threshold == 0:
                enemy_speed += 1

        draw_window()

    else:
        win.fill((0, 0, 0))
        over_text = font.render("Game Over! Press R to Restart", True, (255, 0, 0))
        win.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
