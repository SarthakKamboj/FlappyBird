import pygame


class GameObject:
    def __init__(self, url, scale=None, width=None, height=None):
        self.url = url
        self.scale = scale
        self.height = height
        self.width = width
        self._load_surface()
        self._get_rect()

    def _load_surface(self):
        self.surface = pygame.image.load(self.url)

        if self.scale or self.height or self.width:
            orig_rect = self.surface.get_rect()

            width, height = orig_rect.width, orig_rect.height

            if self.scale:
                width, height = (int(orig_rect.width*self.scale),
                                 int(orig_rect.height*self.scale))
            if self.height:
                height = self.height
            if self.width:
                width = self.width

            self.surface = pygame.transform.scale(
                self.surface, (width, height))

    def _get_rect(self):
        self.rect = self.surface.get_rect()

    def blit(self, screen):
        screen.blit(self.surface, self.rect)
