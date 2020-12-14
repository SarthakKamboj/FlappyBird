import pygame
import time
import numpy as np

class PhysicsGameObject:
    def __init__(self):
        self.rect = pygame.Rect(0,0,0,0)
        self.prev_update_time = time.time()
        self.acc = [0,20]
        self.vel = [0,0]
        # self.time_elapsed_val = 0.01
        self.first_time = True

    def update(self):
        # if self._should_update():
        self._update_vel()
        self.rect = self.rect.move(self.vel)

    def _should_update(self):
        time_elapsed = time.time() - self.prev_update_time
        if time_elapsed >= self.time_elapsed_val:
            self.prev_update_time = time.time()
            return True
        return False


    def _update_vel(self):
        time_elapsed = time.time() - self.prev_update_time
        acc = np.array(self.acc) * time_elapsed
        self.vel = list(np.add(self.vel,acc))
        self.prev_update_time = time.time()