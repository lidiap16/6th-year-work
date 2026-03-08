# Before using this library, it may need to be installed.
# To install the library run the following command:
# pip install pyserial

import serial        # Allows Python to communicate with an external device (e.g. Arduino or micro:bit) using USB
import time          # Allows the program to pause for short periods of time
import csv           # Allows us to write data to a CSV file

ser = serial.Serial()    # Create a serial connection object (this represents the USB connection)
ser.baudrate = 115200    # Set how fast data is sent and received (must match the device's speed - 115200 is speed of a microbit)
ser.port = "COM4"        # Set the USB/COM port the device is connected to
                         # This may need to be changed on a different computer - check in bottom right of Thonny screen
ser.open()               # Open the connection so data can be read from the device

myList = []              # Create an empty list to store the data we receive
count = 0                # Create a counter to keep track of how many readings we take

csvfile = "microbit_readings.csv"   # Name of the CSV file we will write the data to

while count < 11:        # Repeat the code below until we have read data 10 times
    data1 = ser.readline().decode().strip()
    # Read one line of data from the device
    # Convert it from computer bytes into readable text
    # Remove extra spaces and new line characters

    time.sleep(0.5)      # Pause the program for half a second

    print(data1)         # Show the received data on the screen
    myList.append(data1) # Add the received data to the list

    # --- Write the data to the CSV file ---
    # Open the CSV file in append mode ("a") so we do not overwrite previous data
    with open(csvfile, "a", newline="") as f:
        writer = csv.writer(f)       # Create a CSV writer object
        writer.writerow([data1])     # Write the data as a single row in the CSV file
    # ---------------------------------------

    count += 1           # Increase the counter by 1

ser.close()              # Close the connection to the device

print(myList)            # Display the full list of collected data
print("Data has been saved to CSV file:", csvfile)  # Inform the user that the CSV file has been created

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("microbit_readings.csv")

# Split the single column into two
df[['temp','humidity']] = df.iloc[:,0].str.split(",", expand=True).astype(float)

plt.plot(df.index, df["temp"], marker="o", label="Temperature")
plt.plot(df.index, df["humidity"], marker="s", label="Humidity")

plt.legend()
plt.grid(True)
plt.show()


import pygame
import csv
import random
import math

GRID_SIZE = 10
CELL_SIZE = 100
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GREEN = (50, 160, 60)
RED = (200, 50, 50)
BLACK = (30, 30, 30)

# load weather data
weather = []

with open("microbit_readings.csv") as f:
    reader = csv.reader(f)

    next(reader)  # skip header

    for row in reader:
        values = row[0].replace('"','').split(",")
        temp = float(values[0])
        humidity = float(values[1])
        weather.append((temp, humidity))
# weather = []
# with open("microbit_readings.csv") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         weather.append((float(row["temp"]), float(row["humidity"])))

step = 0

# board
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# start infection in center
grid[2][2] = 1

def infection_probability(temp, humidity):
    # peak around 25C using gaussian curve
    temp_factor = math.exp(-((temp - 25) ** 2) / 20)

    humidity_factor = 0
    if humidity > 65:
        humidity_factor = min((humidity - 65) / 35, 1)

    return 0.1 + 0.6 * temp_factor + 0.3 * humidity_factor

def neighbors(x, y):
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for dx,dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            yield nx, ny

def spread(temp, humidity):
    prob = infection_probability(temp, humidity)

    new_grid = [row[:] for row in grid]

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] == 1:
                for nx,ny in neighbors(x,y):
                    if grid[ny][nx] == 0:
                        if random.random() < prob:
                            new_grid[ny][nx] = 1
    return new_grid

running = True
timer = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    timer += clock.get_time()

    if timer > 1000 and step < len(weather):
        temp, humidity = weather[step]
        grid = spread(temp, humidity)
        step += 1
        timer = 0
        print("Step", step, "Temp:", temp, "Humidity:", humidity)

    screen.fill(BLACK)

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = GREEN
            if grid[y][x] == 1:
                color = RED

            pygame.draw.rect(
                screen,
                color,
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 2, CELL_SIZE - 2)
            )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
