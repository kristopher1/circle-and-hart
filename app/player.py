import pygame
from pygame import Surface, SurfaceType


class Player(object):
    _score: int
    _name: str
    _mark: Surface | SurfaceType
    _avatar: Surface | SurfaceType

    def __init__(self, name: str, avatar_file: str, mark_file: str):
        self._name = name
        self._avatar = pygame.image.load('img/' + avatar_file)
        self._mark = pygame.image.load('img/' + mark_file)
        self._score = 0

    def get_name(self):
        return self._name

    def get_mark(self):
        return self._mark

    def get_avatar(self):
        return self._avatar

    def get_score(self):
        return self._score

    def incr_score(self):
        self._score = self._score + 1
