from config import *


class Cell:

    def __init__(self, position, state=State.HEALTHY):
        self.position = position
        self.state = state
        self.rect = pygame.Rect(self.position.x, self.position.y, CELL_SIZE, CELL_SIZE)

    def display(self, window):
        pygame.draw.rect(window, self.state.color, self.rect, 0)