from game_objects.background import Background as Bck
from game_objects.flappy_bird import FlappyBird

class GameLoop:
    def __init__(self,screen):
        self.screen = screen
        self.bck = Bck()
        self.flappy_bird = FlappyBird()       

    def blit(self):
        self.bck.blit(self.screen)
        self.flappy_bird.blit(self.screen)

    def update(self):
        self.bck.move()
        self.flappy_bird.update()