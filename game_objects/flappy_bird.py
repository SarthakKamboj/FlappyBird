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
        self.rot = 0
        self._set_rect_center()
        self.JUMP_VEL = (0,-5)
        self.MAX_ROTATION = 70
        self.MIN_ROTATION = -70
        self.ROTATION_VEL = 3
        self.rotated_surface = None

    def _set_rect_center(self):
        left = self.rect.left
        top = self.rect.top
        height = self.rect.height
        width = self.rect.width


        self.rect.center = (left - (width//2), top - (height//2))

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

    def clamp(self,val,min_val,max_val):
        return min(max_val,max(val,min_val))

    def _rotate(self):
        if self.vel[1] <= 0:
            self.rot += self.ROTATION_VEL
        else:
            self.rot -= self.ROTATION_VEL

        self.rot = self.clamp(self.rot,self.MIN_ROTATION,self.MAX_ROTATION)
        self.rotated_surface = pygame.transform.rotate(self.surface,self.rot)
        self.rect = self.rotated_surface.get_rect(center=self.rect.center)

    def update(self):
        super().update()
        if keyboard.is_pressed("space"):
            self.vel = self.JUMP_VEL
        self._rotate()

    def blit(self,screen):
        if self.rotated_surface:
            screen.blit(self.rotated_surface,self.rect)
        else:
            screen.blit(self.surface,self.rect)
