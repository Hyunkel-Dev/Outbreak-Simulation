import pygame
from pygame.math import Vector2
from script.state import State


# the dimensions of the displayed window
WINDOW_SIZE = Vector2(1280, 720)
# the number of images displayed per second
WINDOW_FPS = 60
# the dimensions of the cells in the grid
CELL_SIZE = 10

# the probability that a healthy cell will be contaminated by an adjacent infected cell
INFECTION_RATE = 0.1
# the probability that an infected cell will die
FATALITY_RATE = 0.05
# the average time (in frames) of healing of a cell
RECOVERY_TIME = 5
# the probability that a healed cell will become immune
IMMUNITY_RATE = 0.2

# the initial rate of infected cells
INFECTED_RATE = 0.001
# the initial rate of vaccinated cells (considered immune)
VACCINATED_RATE = 0.01