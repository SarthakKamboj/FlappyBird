import pygame
import time

class PhysicsGameObject:
    def __init__(self):
        self.rect = pygame.Rect(0,0,0,0)
        self.prev_update_time = time.time()
        self.acc = [0,10]
        self.vel = [0,0]
        self.time_elapsed_val = 0.1

    def update(self):
        if self._should_update():
            self._update_vel()
            self.rect = self.rect.move(self.vel)

    def _should_update(self):
        time_elapsed = time.time() - self.prev_update_time
        if time_elapsed <= self.time_elapsed_val:
            self.prev_update_time = time.time()
            return True
        return False

    def _update_vel(self):
        self.vel[0] += self.acc[0] * self.time_elapsed_val
        self.vel[1] += self.acc[1] * self.time_elapsed_val