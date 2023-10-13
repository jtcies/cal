import pygame


class Base:
    def __init__(self, surface, base_color, occupied_color, base_number):
        self.surface = surface
        self.base_color = base_color
        self.occupied_color = occupied_color
        if base_number == 3:
            self.locaton = pygame.Rect(30, 60, 30, 30)
        elif base_number == 2:
            self.locaton = pygame.Rect(90, 30, 30, 30)
        elif base_number == 1:
            self.locaton = pygame.Rect(150, 60, 30, 30)
        else:
            self.locaton = pygame.Rect(90, 90, 30, 30)

        pygame.draw.rect(surface, base_color, self.locaton, 2)

    def update_base(self, filled):
        if not filled:
            pygame.draw.rect(self.surface, self.base_color, self.locaton, 2)
        else:
            pygame.draw.rect(self.surface, self.occupied_color, self.locaton, 2)
