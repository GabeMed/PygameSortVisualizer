import pygame, random
from algorithms import Algorithms
from animation import Animation

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

random.seed(42)
original_array = [random.randint(1, 20) for _ in range(30)]
working_array = original_array.copy()  # <- cópia para o sort

algorithms = Algorithms(working_array)
algorithms.bubble_sort()  # gera swappedIndexes

animation = Animation(screen, original_array, algorithms.swappedIndexes)
animation.animate()  # reproduz as trocas

pygame.time.wait(1000)  # segura a janela 1 s
pygame.quit()
