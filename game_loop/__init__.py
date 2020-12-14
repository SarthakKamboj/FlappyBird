from game_objects.game_pieces import Background as Bck, FlappyBird, Pipe
# from game_objects.game_pieces.pipe import PipeHead, PipeBody


class GameLoop:
    def __init__(self, screen):
        self.screen = screen
        self.bck = Bck()
        self.flappy_bird = FlappyBird()
        top_height, bottom_height = Pipe.generate_pipe_heights()
        self.pipe = Pipe(PIPE_HEIGHT=bottom_height)

    def blit(self):
        self.bck.blit(self.screen)
        self.flappy_bird.blit(self.screen)
        self.pipe.blit(self.screen)

    def update(self):
        self.bck.move()
        self.flappy_bird.update()
