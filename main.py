from config import *
import sys

from script.grid import Grid

if __name__ == '__main__':

    pygame.init()
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Outbreak Simulation")

    icon = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(icon)

    grid = Grid()

    run = True
    while run:

        if grid.finished:
            run = False
        else:
            grid.update()
        grid.display(window)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    if not run:
        grid.display_curves()
        pygame.quit()
        sys.exit()

    pygame.time.wait(1000 // WINDOW_FPS)