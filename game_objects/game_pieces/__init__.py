import pygame
import keyboard
import numpy as np
from ..physics_objects import ColliderPhysicsObject, PhysicsGameObject
from .pipe import PipeBody, PipeHead
from ..gameobject import GameObject
import pygame

class Pipe():
    def __init__(self):
        pass

class FlappyBird(PhysicsGameObject,GameObject):
    def __init__(self):
        FLAPPY_BIRD_URL = "images/flappy_bird.png"
        SCALE = 0.1
        PhysicsGameObject.__init__(self)
        GameObject.__init__(self,URL=FLAPPY_BIRD_URL,SCALE=SCALE)
        self._update_initial_pos()
        self._set_rect_center()
        self._init_variables()

    def _init_variables(self):
        self.rot = 0
        self.JUMP_VEL = (0,-7.5)
        self.MAX_ROTATION = 20
        self.MIN_ROTATION = -80
        self.ROTATION_VEL = 1.5
        self.ROTATION_TURNING_POINT_VEL = 7
        self.rotated_surface = None
       

    def _set_rect_center(self):
        left = self.rect.left
        top = self.rect.top
        height = self.rect.height
        width = self.rect.width
        self.rect.center = (left - (width//2), top - (height//2))

    def _update_initial_pos(self):
        width, height = pygame.display.get_surface().get_size()
        self.rect.top = (height // 2) - (self.rect.height // 2)
        self.rect.left = width * 0.2

    def clamp(self,val,min_val,max_val):
        return min(max_val,max(val,min_val))

    def _rotate(self):
        if self.vel[1] >= self.ROTATION_TURNING_POINT_VEL:
            self.rot -= 10
        else:
            self.rot += 20

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


class BackgroundSurface(GameObject):
    def __init__(self,INIT_X):
        BCK_URL = "images/bck.PNG"
        super().__init__(BCK_URL)
        self.rect.left = INIT_X
        self.SPEED = [-2,0]

    def get_image(self):
        return self.surface
    
    def get_rect(self):
        return self.rect

    def get_width(self):
        return self.rect.width

    def _slide(self):
        window_width, _ = pygame.display.get_surface().get_size()
        if self.rect.left < -self.get_width():
            self.rect.left = window_width

    def move(self):
        self.rect = self.rect.move(self.SPEED)
        self._slide()
    
class Background:
    def __init__(self):
        self._generate_bck_surfaces()

    def _generate_bck_surfaces(self):
        self.bcks = []
        window_width, _ = pygame.display.get_surface().get_size()
        cur_bck_width = 0
        while cur_bck_width < window_width:
            self.bcks.append(BackgroundSurface(cur_bck_width))
            cur_bck_width += self.bcks[-1].get_width()
        self.bcks.append(BackgroundSurface(cur_bck_width))

    def move(self):
        for bck in self.bcks:
            bck.move()

    def blit(self,screen):
        for bck in self.bcks:
            bck.blit(screen)