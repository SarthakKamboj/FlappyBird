# from .collider_gameobject import ColliderPhysicsObject
from ..physics_objects import ColliderPhysicsObject
from ..gameobject import GameObject
import pygame

class PipeHead(ColliderPhysicsObject,GameObject):
    def __init__(self):
        HEAD_URL = "images/pipes/head.PNG"
        # super(ColliderPhysicsObject, self).__init__()
        GameObject.__init__(self,HEAD_URL)


    def blit(self,screen):
        screen.blit(self.surface,self.rect)

        # self._load_pipe_head_surface()
    
    # def _load_pipe_head_surface(self):
    #     HEAD_URL = "images/pipes/head.PNG"

    #     self.surface = pygame.image.load(HEAD_URL)

    #     self.rect = self.surface.get_rect()


class PipeBody(ColliderPhysicsObject):
    def __init__(self):
        super().__init__()
        self._load_pipe_body_surface()
    
    def _load_pipe_body_surface(self):
        BODY_URL = "images/pipes/body.PNG"
        self.surface = pygame.image.load(BODY_URL)
        self.rect = self.surface.get_rect()




