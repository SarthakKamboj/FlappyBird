from ..physics_objects import ColliderPhysicsObject
from ..gameobject import GameObject
import pygame
import random

PIPE_IMAGES_BASE_URL = "images/pipes"
PIPE_WIDTH = 90


class PipeHead(ColliderPhysicsObject, GameObject):
    def __init__(self, top=None, bottom=None):
        HEAD_URL = PIPE_IMAGES_BASE_URL + "/head.PNG"
        PIPE_HEAD_HEIGHT = PIPE_WIDTH//2
        GameObject.__init__(self, url=HEAD_URL,
                            height=PIPE_HEAD_HEIGHT, width=PIPE_WIDTH)
        ColliderPhysicsObject.__init__(self)

        SCREEN_HEIGHT = pygame.display.get_surface().get_height()

        if top is not None:
            self.rect.top = top
        elif bottom is not None:
            self.rect.top = SCREEN_HEIGHT - bottom - self.rect.height


class PipeBody(ColliderPhysicsObject, GameObject):
    def __init__(self,  height, top=None, bottom=None):

        PIPE_WIDTH_RATIO = 0.9
        PIPE_BODY_WIDTH = int(PIPE_WIDTH * PIPE_WIDTH_RATIO)
        PIPE_BODY_PADDING = int(PIPE_WIDTH * ((1-PIPE_WIDTH_RATIO)/2))

        BODY_URL = PIPE_IMAGES_BASE_URL + "/body.PNG"

        ColliderPhysicsObject.__init__(self)
        GameObject.__init__(self, url=BODY_URL,
                            width=PIPE_BODY_WIDTH, height=height)
        self.rect.left += PIPE_BODY_PADDING

        SCREEN_HEIGHT = pygame.display.get_surface().get_height()

        if top is not None:
            self.rect.top = top
        elif bottom is not None:
            self.rect.top = SCREEN_HEIGHT - bottom - self.rect.height

    def get_height(self):
        return self.rect.height
