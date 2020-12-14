import pygame


class GameObject:
    def __init__(self,URL,SCALE=None,WIDTH=None,HEIGHT=None):
        self.URL = URL
        self.SCALE = SCALE
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self._load_surface()
        self._get_rect()

    def _load_surface(self):
        self.surface = pygame.image.load(self.URL)

        if self.SCALE or self.HEIGHT or self.WIDTH:
            orig_rect = self.surface.get_rect()

            WIDTH, HEIGHT = orig_rect.width, orig_rect.height

            if self.SCALE:
                WIDTH,HEIGHT = (int(orig_rect.width*self.SCALE),int(orig_rect.height*self.SCALE))
            if self.HEIGHT:
                HEIGHT = self.HEIGHT
            if self.WIDTH:
                WIDTH = self.WIDTH

            self.surface = pygame.transform.scale(self.surface,(WIDTH,HEIGHT))

    def _get_rect(self):
        self.rect = self.surface.get_rect()

    def blit(self,screen):
        screen.blit(self.surface,self.rect)