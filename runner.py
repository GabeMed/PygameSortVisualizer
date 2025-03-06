import pygame
import random
from algorithms import Algorithms

# initializing pygame and setting some config
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# getting the random array
random.seed(42)
array = [random.randint(1, 20) for _ in range(10)]

# Creating the sorting algorithm object
algorithms = Algorithms(array, screen)

# Running pygame
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Perform the sorting algorithm with animation
    algorithms.bubble_sort(style="Rect")
    running = False  # Stop after sorting

    # Control the frame rate
    clock.tick(60)

pygame.quit()
