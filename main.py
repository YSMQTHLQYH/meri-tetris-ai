import pygame
from enum import Enum
from pygame_human_game import *

pygame.init()

screen = pygame.display.set_mode((480, 640))
clock = pygame.time.Clock()

game = PygameHumanGame()
while game.loop():
    screen.fill((30, 30, 30))
    game.surface.update(game.player, game.player.current_piece)
    screen.blit(game.surface.surface)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()