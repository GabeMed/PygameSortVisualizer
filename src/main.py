import pygame, random
from algorithms import Algorithms
from animation import Animation

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

random.seed(42)
original_array = [random.randint(1, 20) for _ in range(30)]
working_array = original_array.copy()  # Copy the original array to avoid modifying it

algorithms = Algorithms(working_array)
algorithms.quick_sort()  # Execute the sorting algorithm and store the swaps

animation = Animation(screen, original_array, algorithms.swappedIndexes)
animation.animate()  # Animate the sorting process

pygame.time.wait(1000)  # Wait for a second before closing
pygame.quit()
