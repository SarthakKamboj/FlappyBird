import sys
import time
import pygame
from game_loop import GameLoop

pygame.init()

SIZE = WIDTH, HEIGHT = 1300, 700
BLACK = (0, 0, 0)
FPS = 60
WAIT_TIME = 1 / FPS 

screen = pygame.display.set_mode(SIZE)
game_loop = GameLoop(screen)

if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(BLACK)
        game_loop.blit()
        game_loop.update()
        pygame.display.flip()
        time.sleep(WAIT_TIME)
