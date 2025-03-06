from animation import Animation
import pygame


class Algorithms:
    def __init__(self, array: list, screen):
        self.array = array
        self.animation = Animation(screen, array)

    def bubble_sort(self, style=None):
        n = len(self.array)
        for i in range(n):
            swapped = False
            for j in range(n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.animation.swap(j, j + 1)
                    swapped = True

                if style == None or "rect":
                    # Update the frame and highlight swapped bars
                    self.animation.frameRect(highlight=(j, j + 1))
                    pygame.time.delay(100)  # Adjust delay as needed for visibility

                elif style == "bubble":
                    # Swipe the bubbles
                    self.animation.frameBubble
                    pygame.time.delay(100)

            if not swapped:
                break
        # Final update to show sorted array
        self.animation.frame()
