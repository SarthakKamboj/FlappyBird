import pygame

class BackgroundSurface:
    def __init__(self,INIT_X):
        BCK_URL = "images/bck.PNG"
        self.bck = pygame.image.load(BCK_URL)
        self.bck_rect = self.bck.get_rect()
        self.bck_rect.left = INIT_X
        self.SPEED = [-2,0]

    def get_image(self):
        return self.bck
    
    def get_rect(self):
        return self.bck_rect

    def get_width(self):
        return self.bck_rect.width

    def _slide(self):
        window_width, _ = pygame.display.get_surface().get_size()
        if self.bck_rect.left < -self.get_width():
            self.bck_rect.left = window_width

    def move(self):
        self.bck_rect = self.bck_rect.move(self.SPEED)
        self._slide()

    def blit(self,screen):
        screen.blit(self.bck,self.bck_rect)
        
    
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