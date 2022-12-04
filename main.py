import pygame, sys
import random

#pygame starten mit init
pygame.init()
window_width = 450
window_height = 800
window = pygame.display.set_mode((window_width,window_height))
refresh_rate = 120
FPS = pygame.time.Clock()

backround = pygame.image.load('textures/bg.png').convert()

ground = pygame.image.load('textures/base.png').convert()
ground = pygame.transform.scale(ground,(window.get_height(), ground.get_height()))

ground_x = 0
backround_x = 0

player_down = pygame.transform.scale2x(pygame.image.load('player/yellowbird-downflap.png').convert())
player_mid = pygame.transform.scale2x(pygame.image.load('player/yellowbird-midflap.png').convert())
player_up = pygame.transform.scale2x(pygame.image.load('player/yellowbird-upflap.png').convert())

player_animation = [player_up, player_mid, player_down]

player = player_animation[0]
player_rect = player.get_rect(center=(100,400))
player_move = 1

PLAYEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PLAYEREVENT, 150)
player_counter = 0

obstacle = pygame.image.load('textures/pipe.png').convert()
obstacle = pygame.transform.scale2x(obstacle)
obstacle_choices = [700,800,900,1000]
obstacles = []

SPAWNOBSTACLE = pygame.USEREVENT
pygame.time.set_timer(SPAWNOBSTACLE, 1000)

collision = False

def collisions(obstacles, player_rect):
    if player_rect.centery < 15 or player_rect.centery > 720:
        return True

    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            return True

    return False



def create_obstacle():
    obstacle_height = random.choice(obstacle_choices)
    obstacle_rect_normal = obstacle.get_rect(center = (700, obstacle_height))
    obstacle_rect_flip = obstacle.get_rect(center = (700, obstacle_height - 1000))
    return(obstacle_rect_normal, obstacle_rect_flip)


def draw_obstacles(obstacles):
    for obstacle_i in obstacles:
        if obstacle_i.bottom >= 800:
            window.blit(obstacle, obstacle_i)
        else:
            new_obstacle = pygame.transform.flip(obstacle, False, True)
            window.blit(new_obstacle, obstacle_i)


def move_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle.centerx -= 3

#gameloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_move = 0
                player_move -= 7

        if event.type == SPAWNOBSTACLE:
            obstacles.extend(create_obstacle())

        if event.type == PLAYEREVENT:
            player = player_animation[player_counter % 3]
            player_counter += 1




    window.blit(backround, (backround_x,0))
    window.blit(backround, (backround_x + window_width,0))
    backround_x -=0.5
    if abs(backround_x) == window_width:
        backround_x = 0
    window.blit(ground, (ground_x,720))
    window.blit(ground, (ground_x + window_width,720))
    ground_x -= 1.5
    if abs(ground_x) == window_width:
        ground_x = 0


    if collision is not True:
        window.blit(player, player_rect)
        player_move += 0.2
        player_rect.centery += player_move

        draw_obstacles(obstacles)
        move_obstacles(obstacles)

        collison = collisions(obstacles, player_rect)

    FPS.tick(refresh_rate)
    pygame.display.update()






