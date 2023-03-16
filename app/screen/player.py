from math import floor

import pygame
from pygame import Rect

from app.player import Player
from app.screen.screen import Screen


class PlayerScreen(object):
    _name_rect: Rect
    _avatar_rect: Rect
    _player: Player
    _rect: Rect
    _screen: Screen
    SCREEN_WIDTH = 250
    SCREEN_HEIGHT = 64
    FONT = 'freesansbold.ttf'
    FONT_COLOR = 'white'
    FONT_SIZE = 32

    def __init__(self, screen: Screen, player: Player, x: int, y: int):
        self._screen = screen
        self._player = player
        if x < 0:
            x = screen.width + x - PlayerScreen.SCREEN_WIDTH
        (avatar_width, avatar_height) = player.get_avatar().get_size()
        self._font = pygame.font.Font(PlayerScreen.FONT, PlayerScreen.FONT_SIZE)
        self._rect = pygame.Rect(x, y, PlayerScreen.SCREEN_WIDTH, PlayerScreen.SCREEN_HEIGHT)
        self._avatar_rect = pygame.Rect((x, y), (avatar_width, avatar_height))
        name_y = y + floor((PlayerScreen.SCREEN_HEIGHT - PlayerScreen.FONT_SIZE) / 2)
        self._name_rect = pygame.Rect(x + avatar_width + 10, name_y, PlayerScreen.SCREEN_WIDTH - avatar_width - 10,
                                      PlayerScreen.FONT_SIZE)

    def draw(self):
        box_text = self._font.render(self._player.get_name() + ' : ' + str(self._player.get_score()), False,
                                     PlayerScreen.FONT_COLOR)
        self._screen.get_surface().blit(box_text, self._name_rect)
        self._screen.get_surface().blit(self._player.get_avatar(), self._avatar_rect)
