from ..physics_objects import ColliderPhysicsObject
from ..gameobject import GameObject
import pygame
import random

PIPE_BODY_WIDTH = 75
PIPE_HEAD_WIDTH = int(PIPE_BODY_WIDTH * 1.25)
PIPE_IMAGES_BASE_URL = "images/pipes"

class PipeHead(ColliderPhysicsObject,GameObject):
    def __init__(self):
        HEAD_URL = f"{PIPE_IMAGES_BASE_URL}/head.PNG"
        GameObject.__init__(self,HEAD_URL,WIDTH=PIPE_HEAD_WIDTH)
        ColliderPhysicsObject.__init__(self)


class PipeBody(ColliderPhysicsObject,GameObject):
    def __init__(self):
        MIN_HEIGHT = 10
        MAX_HEIGHT = 200
        HEIGHT = random.randint(MIN_HEIGHT,MAX_HEIGHT)
        BODY_URL = f"{PIPE_IMAGES_BASE_URL}/body.PNG"
        ColliderPhysicsObject.__init__(self)
        GameObject.__init__(self,URL=BODY_URL,WIDTH=PIPE_BODY_WIDTH,HEIGHT=HEIGHT)


