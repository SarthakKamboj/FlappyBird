from ..physics_objects import ColliderPhysicsObject
from ..gameobject import GameObject
import pygame

class PipeHead(ColliderPhysicsObject,GameObject):
    def __init__(self):
        HEAD_URL = "images/pipes/head.PNG"
        GameObject.__init__(self,HEAD_URL)
        ColliderPhysicsObject.__init__(self)


class PipeBody(ColliderPhysicsObject,GameObject):
    def __init__(self):
        BODY_URL = "images/pipes/body.PNG"
        ColliderPhysicsObject.__init__(self)
        GameObject.__init__(self,BODY_URL)
        # self._load_pipe_body_surface()
    
    # def _load_pipe_body_surface(self):
    #     self.surface = pygame.image.load(BODY_URL)
    #     self.rect = self.surface.get_rect()




