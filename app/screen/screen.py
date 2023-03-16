import pygame
from pygame import Surface


class Screen(object):
    _surface: Surface

    def __init__(self):
        self.width = 700
        self.height = 700

    def init(self):
        pygame.init()
        # set window icon
        icon = pygame.image.load('img/icon.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Kołko i serce')
        self._surface = pygame.display.set_mode([self.width, self.height])
        self.draw()

    def draw(self):
        self._surface.fill((0, 0, 0))
        background = pygame.image.load('img/background_700.jpg')
        self._surface.blit(background, (0, 0))

    def get_surface(self):
        return self._surface

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
