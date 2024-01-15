import pygame
import sys

#start pygame
pygame.init()

#Constant variables for the GUI
WINDOW_SIZE = (450, 450)
GRID_SIZE = 9
CELL_SIZE = WINDOW_SIZE[0] // GRID_SIZE
FONT = pygame.font.SysFont('Arial', 40)

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#0 represents empty cells
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


pygame.quit()
sys.exit()