import numpy as np
import pygame
import random

# colors
background_color = "#222222"
cell_color = "#FFFF00"

def init(width, height):
    cells = [[0 for i in range(height)] for j in range(width)]
    
    for i in range(width):
        for j in range(height):
            cells[i][j] = 1 if random.random() < 0.07 else 0
    
    return cells

def evolution(surface, cells, cell_size, width, height):
    temp = cells.copy()

    for x in range(width):
        for y in range(height):
            around = np.sum([row[(y-1)%height:(y+2)%height] for row in temp[(x-1)%width:(x+2)%width]]) - temp[x][y]
            temp[x][y] = 1 if around==3 or (around==2 and temp[x][y]) else 0
        
            color = background_color if temp[x][y] == 0 else cell_color
            pygame.draw.rect(surface, color, (x*cell_size, y*cell_size, cell_size-1, cell_size-1))
    
    return temp

def createGame(width, height, cell_size):
    pygame.init()
    pygame.display.set_caption("Game of Life")
    surface = pygame.display.set_mode((width * cell_size, height * cell_size))
    cells = init(width, height)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                return

        surface.fill(background_color)
        cells = evolution(surface, cells, cell_size, width, height)
        pygame.display.update()

if __name__ == "__main__":
    createGame(110, 100, 10)

