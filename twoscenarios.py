import pygame
import random
import math
##

import matplotlib.pyplot as plt

time_steps = []
infected_A = []
infected_B = []
step = 0

GRID_SIZE = 8
CELL_SIZE = 80
MARGIN = 60

WIDTH = GRID_SIZE * CELL_SIZE * 2 + MARGIN
HEIGHT = GRID_SIZE * CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tree Fungus Spread Comparison")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
# 
GREEN = (50,160,60)
RED = (200,50,50)
BLACK = (30,30,30)
WHITE = (240,240,240)

#2scenarios 
scenarioA = {"temp":32, "humidity":50}  #hot and dry
scenarioB = {"temp":25, "humidity":75}  #ideal fungus conditions


healthy_tree = pygame.image.load("healthy_tree.png")
infected_tree = pygame.image.load("infected_tree.png")

healthy_tree = pygame.transform.scale(healthy_tree, (CELL_SIZE, CELL_SIZE))
infected_tree = pygame.transform.scale(infected_tree, (CELL_SIZE, CELL_SIZE))

#creates two boards
gridA = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]
gridB = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]

#starts infection in center
gridA[2][2] = 1
gridB[2][2] = 1
##
def count_infected(grid):
    return sum(sum(row) for row in grid)


def infection_probability(temp, humidity):

    temp_factor = math.exp(-((temp - 25)**2)/20) #This creates a bell curve centered at 25°C
# Temp    Spread
# 15°C    low
# 20°C    medium
# 25°C    highest
# 30°C    lower
# 35°C    very low

    humidity_factor = 0
    if humidity > 65:
        humidity_factor = min((humidity - 65)/35,1) #humidity- 65 normalises the range and dividing by 35 creates a fraction, and
        #(35,1) and min make sure it doesnt exceed 1

# below 65% → little spread
# above 65% → increasing spread

    return 0.05 + 0.6*temp_factor + 0.35*humidity_factor
#0.05% chance of infectio olways present in forests
#0.6 multiplied by the temperature as temp playes an extremely big part in fungi spread especialy fungal pathogen – Hymenoscyphus fraxineus
#0.35 multiplied by humidity as it also playes a big part in the spread of the fungus

def neighbors(x,y):

    dirs = [(-1,0),(1,0),(0,-1),(0,1)]

    for dx,dy in dirs:
        nx,ny = x+dx,y+dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            yield nx,ny


def spread(grid,temp,humidity):

    prob = infection_probability(temp,humidity)

    new = [row[:] for row in grid]

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):

            if grid[y][x] == 1:

                for nx,ny in neighbors(x,y):
                    if grid[ny][nx] == 0:
                        if random.random() < prob:
                            new[ny][nx] = 1

    return new


timer = 0
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    timer += clock.get_time()

    if timer > 1200:
        
        gridA = spread(gridA, scenarioA["temp"], scenarioA["humidity"])
        gridB = spread(gridB, scenarioB["temp"], scenarioB["humidity"])

        step += 1

        time_steps.append(step)
        infected_A.append(count_infected(gridA))
        infected_B.append(count_infected(gridB))

        timer = 0

    screen.fill(BLACK)

    # draw scenario A
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):

            color = GREEN
            if gridA[y][x] == 1:
                color = RED

            if gridA[y][x] == 1:
                screen.blit(infected_tree, (x*CELL_SIZE, y*CELL_SIZE))
            else:
                screen.blit(healthy_tree, (x*CELL_SIZE, y*CELL_SIZE))

    # draw scenario B
    offset = GRID_SIZE*CELL_SIZE + MARGIN

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):

            color = GREEN
            if gridB[y][x] == 1:
                color = RED

            if gridB[y][x] == 1:
                screen.blit(infected_tree, (offset + x*CELL_SIZE, y*CELL_SIZE))
            else:
                screen.blit(healthy_tree, (offset + x*CELL_SIZE, y*CELL_SIZE))

    # labels for pygame model
    textA = font.render("Hot & Dry", True, WHITE)
    textB = font.render("Warm & Humid", True, WHITE)

    screen.blit(textA, (80, HEIGHT-30))
    screen.blit(textB, (offset+60, HEIGHT-30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

plt.plot(time_steps, infected_A, label="Hot & Dry", color="orange")
plt.plot(time_steps, infected_B, label="Warm & Humid", color="green")

plt.xlabel("Time Step")
plt.ylabel("Infected Trees")
plt.title("Fungal Infection Spread")
plt.legend()
plt.grid(True)

plt.show()