import pygame


class Animation:
    def __init__(self, screen, array: list, swappedIndexes: list[list]):
        self.screen = screen
        self.array = array
        self.positions = []
        self.swappedIndexes = swappedIndexes

        # Calculate initial positions
        self.calculate_positions()

    def calculate_positions(self):
        screen_width, _ = self.screen.get_size()
        bar_gap = 10
        bar_width = (screen_width - bar_gap * (1 + len(self.array))) / len(self.array)
        self.positions = [
            bar_gap * (i + 1) + bar_width * i for i in range(len(self.array))
        ]
        self.bar_width = bar_width

    def frameRect(self, highlight=None):
        _, screen_height = self.screen.get_size()
        self.screen.fill("black")

        for i, value in enumerate(self.array):
            color = pygame.Color(0, 0, 255)
            if highlight and i in highlight:
                color = pygame.Color(255, 0, 0)
            pygame.draw.rect(
                self.screen,
                color,
                pygame.Rect(
                    self.positions[i],
                    screen_height - (screen_height * 0.05 * value),
                    self.bar_width,
                    screen_height * 0.05 * value,
                ),
            )

        pygame.display.update()

    def animate(self):
        for i, j in self.swappedIndexes:
            # aplica a troca no vetor mostrado
            self.array[i], self.array[j] = self.array[j], self.array[i]
            # redesenha destacando as duas barras trocadas
            self.frameRect(highlight=(i, j))
            pygame.time.delay(100)

        self.frameRect()  # frame final sem destaque
