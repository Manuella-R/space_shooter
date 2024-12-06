import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cannon Shooter Game")

font = pygame.font.SysFont(None, 36)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

clock = pygame.time.Clock()

# Load assets
shoot_sound = pygame.mixer.Sound("shot.wav")
explosion_sound = pygame.mixer.Sound("grenade.wav")

# Load images
player_folder = "player"
enemy_folder = "enemies"
damage_folder = "damage"
background_folder = "background"

player_images = [pygame.image.load(os.path.join(player_folder, img)) for img in os.listdir(player_folder)]
enemy_images = [pygame.image.load(os.path.join(enemy_folder, img)) for img in os.listdir(enemy_folder)]
damage_images = [pygame.image.load(os.path.join(damage_folder, img)) for img in os.listdir(damage_folder)]
background_images = [pygame.image.load(os.path.join(background_folder, img)) for img in os.listdir(background_folder)]
background = random.choice(background_images)  # Choose a random background

# Variables
cannon_speed = 5
bullet_speed = -7
spheres = []
sphere_speed = 2
power_ups = []
lives = 3
shield_active = False
shield_timer = 0
level = 1
score = 0
player_model = None
bullets = []
last_shot_time = 0
cooldown_duration = 100
paused = False


# Functions
def intro_screen():
    screen.blit(pygame.transform.scale(background, (WIDTH, HEIGHT)), (0, 0))
    title = font.render("Cannon Shooter Game", True, WHITE)
    start_text = font.render("Press 'S' to Start", True, WHITE)
    exit_text = font.render("Press 'E' to Exit", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
    screen.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + 50))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            return
        elif keys[pygame.K_e]:
            pygame.quit()
            sys.exit()


def choose_model():
    global player_model
    screen.blit(pygame.transform.scale(background, (WIDTH, HEIGHT)), (0, 0))
    title = font.render("Choose Your Model", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    for i, model in enumerate(player_images):
        x = (i % 5) * (WIDTH // 5) + 20
        y = HEIGHT // 3
        screen.blit(pygame.transform.scale(model, (60, 60)), (x, y))
        model_num = font.render(str(i + 1), True, BLACK)
        screen.blit(model_num, (x + 25, y + 70))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        for i in range(5):
            if keys[pygame.K_1 + i]:
                player_model = pygame.transform.scale(player_images[i], (50, 50))
                return


def draw_background():
    screen.blit(pygame.transform.scale(background, (WIDTH, HEIGHT)), (0, 0))


def draw_cannon(x, y):
    screen.blit(player_model, (x, y))


def draw_bullets(bullets):
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

