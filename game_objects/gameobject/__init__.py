import pygame


class GameObject:
    def __init__(self,URL,SCALE=None):
        self.URL = URL
        self.SCALE = SCALE
        self._load_surface()
        self._get_rect()

    def _load_surface(self):
        if not self.SCALE:
            self.surface = pygame.image.load(self.URL)
        else:
            orig_surface = pygame.image.load(self.URL)
            orig_rect = orig_surface.get_rect()
            SCALED_DIM = (int(orig_rect.width*self.SCALE),int(orig_rect.height*self.SCALE))
            self.surface = pygame.transform.scale(orig_surface,SCALED_DIM)

    def _get_rect(self):
        self.rect = self.surface.get_rect()

    def blit(self,screen):
        screen.blit(self.surface,self.rect)