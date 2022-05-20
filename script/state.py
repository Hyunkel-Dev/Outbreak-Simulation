from enum import Enum


class State(Enum):
    HEALTHY = ("Healthy", (44, 110, 73), "#2C6E49")
    INFECTED = ("Infected", (255, 16, 83), "#FF1053")
    IMMUNIZED = ("Immunized", (34, 116, 165), "#2274A5")
    DEAD = ("Dead", (13, 22, 11), "#0D160B")

    @property
    def name(self):
        return self.value[0]

    @property
    def color(self):
        return self.value[1]

    @property
    def hex_color(self):
        return self.value[2]