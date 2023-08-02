import pygame
import math
from settings import * 
from player import Player
from map import world_map
from ray_casting import ray_casting

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    player.movement()
    sc.fill(DARKGRAY)
    
    pygame.draw.rect(sc, SKYBLUE, (0,0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, PURLE, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    
    ray_casting(sc, (player.pos), player.angle)
    
    # pygame.draw.circle(sc, GREEN, (int(player.x),int(player.y)),12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle),player.y + WIDTH * math.sin(player.angle)))
    
    # for x,y in world_map:
    #     pygame.draw.rect(sc, BLUE, (x,y, TILE, TILE), 2)
    
    pygame.display.flip()
    clock.tick(FPS)        