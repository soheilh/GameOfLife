from random import random
import os
import time

# for draw in terminal
def draw(matrix, w, h):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(h):
        for j in range(w):
            print("■" if matrix[i][j] else " ", end="")
        print('', end='\n')

# for calculate the number of lives in around (x,y)
def calcAround(matrix, w, h, x, y):
    lives = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if matrix[j%h][i%w]:
                lives += 1

    if matrix[y][x]:
        lives -= 1

    return lives

# for update in each iteration
def evolution(matrix, w, h):
    tempList = matrix.copy()
    for i in range(w):
        for j in range(h):
            around = calcAround(matrix, w, h, i, j)
            tempList[j][i] = 1 if around==3 or (around==2 and tempList[j][i]) else 0

    matrix = tempList.copy()



w = 50
h = 50

matrix = [[0 for x in range(w)] for y in range(h)]

for i in range(w):
    for j in range(h):
        matrix[j][i] = 1 if (random()<=0.07) else 0
        
while(1):
    draw(matrix, w, h)
    evolution(matrix, w, h)
    time.sleep(0.3)