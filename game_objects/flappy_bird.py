import pygame
import keyboard
from game_objects.physics_gameobject import PhysicsGameObject
import numpy as np

class FlappyBird(PhysicsGameObject):
    def __init__(self):
        super().__init__()
        self._load_surface()        
        self.rect = self.surface.get_rect()
        self._update_initial_pos()
        self.JUMP_VEL = (0,-5)

    def _load_surface(self):
        FLAPPY_BIRD_URL = "images/flappy_bird.png"
        SCALE = 0.1

        orig_fp = pygame.image.load(FLAPPY_BIRD_URL)
        orig_fp_rect = orig_fp.get_rect()
        SCALED_FLAPPY_BIRD_DIMENSIONS = (int(orig_fp_rect.width * SCALE), int(orig_fp_rect.height * SCALE))

        self.surface = pygame.transform.scale(orig_fp,SCALED_FLAPPY_BIRD_DIMENSIONS)


    def _update_initial_pos(self):
        width, height = pygame.display.get_surface().get_size()
        self.rect.top = (height // 2) - (self.rect.height // 2)
        self.rect.left = width * 0.2


    def update(self):
        super().update()
        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:
        #             print("space pressed")
        if keyboard.is_pressed("space"):
        #     print("hello")
                    # self.vel = np.add(self.jump_vel,self.vel)
            print("hello")
            self.vel = self.JUMP_VEL
                    # self.vel += self.jump_vel

    def blit(self,screen):
        screen.blit(self.surface,self.rect)