from config import *
from script.cell import Cell
import random
import matplotlib.pyplot as plt


class Grid:

    def __init__(self):
        self.size = WINDOW_SIZE // CELL_SIZE
        self.quantity = self.size.x * self.size.y

        self.cells = [[Cell(Vector2(x, y) * CELL_SIZE) for x in range(int(self.size.x))] for y in range(int(self.size.y))]

        self.data = {
            State.HEALTHY: [self.quantity - int(INFECTED_RATE * self.quantity) - int(VACCINATED_RATE * self.quantity)],
            State.INFECTED: [int(INFECTED_RATE * self.quantity)],
            State.IMMUNIZED: [int(VACCINATED_RATE * self.quantity)],
            State.DEAD: [0]
        }

        self.create_virus()

        self.finished = False
        self.had_displayed_curves = False

    def display(self, window):
        for line in self.cells:
            for cell in line:
                cell.display(window)

    def get_neighbors(self, position, cells):
        result = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i != 0 or j != 0:
                    new_position = position + Vector2(i, j)
                    if 0 <= new_position.x < self.size.x and 0 <= new_position.y < self.size.y:
                        result.append(cells[int(new_position.y)][int(new_position.x)])
        return result

    def update(self):
        for array in self.data.values():
            array.append(array[-1])

        cells_copy = [line[:] for line in self.cells]
        for line in cells_copy:
            for cell in line:
                if cell.state == State.INFECTED and random.random() < FATALITY_RATE / RECOVERY_TIME:
                    cell.state = State.DEAD
                    self.data[State.DEAD][-1] += 1
                    self.data[State.INFECTED][-1] -= 1
                elif cell.state == State.INFECTED and random.random() < 1 / RECOVERY_TIME:
                    if random.random() < IMMUNITY_RATE:
                        cell.state = State.IMMUNIZED
                        self.data[State.IMMUNIZED][-1] += 1
                    else:
                        cell.state = State.HEALTHY
                        self.data[State.HEALTHY][-1] += 1
                    self.data[State.INFECTED][-1] -= 1
                elif cell.state == State.HEALTHY:
                    position = cell.position // CELL_SIZE
                    for neighbor in self.get_neighbors(position, cells_copy):
                        if neighbor.state == State.INFECTED and random.random() < INFECTION_RATE:
                            cell.state = State.INFECTED
                            self.data[State.INFECTED][-1] += 1
                            self.data[State.HEALTHY][-1] -= 1
                            break
        self.cells = cells_copy

        if not self.data[State.INFECTED][-1]:
            self.finished = True

    def create_virus(self):
        for state in (State.INFECTED, State.IMMUNIZED):
            for _ in range(self.data[state][0]):
                cond = True
                while cond:
                    y = random.randint(0, len(self.cells) - 1)
                    x = random.randint(0, len(self.cells[0]) - 1)
                    cond = self.cells[y][x].state != State.HEALTHY
                    if not cond:
                        self.cells[y][x].state = state

    def display_curves(self):
        for state, array in self.data.items():
            self.data[state] = [value * 100 / self.quantity for value in array]

        if not self.had_displayed_curves:
            legend = []
            for state, array in self.data.items():
                plt.plot(list(range(len(array))), array, state.hex_color)
                legend.append(state.name)
            plt.legend(legend)
            plt.show()
            self.had_displayed_curves = True