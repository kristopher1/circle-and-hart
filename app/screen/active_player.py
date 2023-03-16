from math import floor

import pygame
from pygame import Rect
from pygame.font import Font

from app.game_event import GameEvent
from app.player import Player
from app.screen.screen import Screen
from event.event_dispatcher import EventDispatcher


class ActivePlayerScreen(object):
    _font: Font
    _active_player: Player
    _event_dispatcher: EventDispatcher
    _rect: Rect
    _screen: Screen
    SCREEN_WIDTH = 250
    SCREEN_HEIGHT = 64
    FONT = 'freesansbold.ttf'
    FONT_COLOR = 'white'
    FONT_SIZE = 32

    def __init__(self, screen: Screen, event_dispatcher: EventDispatcher, active_player: Player, y: int):
        self._screen = screen
        self._event_dispatcher = event_dispatcher.add_event_listener(GameEvent.ACTIVE_PLAYER_SET,
                                                                     self.on_active_player_set)
        self._y = y
        self._active_player = active_player

    def init(self):
        self._font = pygame.font.Font(ActivePlayerScreen.FONT, ActivePlayerScreen.FONT_SIZE)
        x = (self._screen.get_width() / 2) - (ActivePlayerScreen.SCREEN_WIDTH / 2)
        self._rect = pygame.Rect(x, self._y, ActivePlayerScreen.SCREEN_WIDTH, ActivePlayerScreen.SCREEN_HEIGHT)

    def on_active_player_set(self, event_data: GameEvent):
        self._active_player = event_data.data

    def draw(self):
        if self._active_player:
            box_text = self._font.render('Gracz : ' + str(self._active_player.get_name()), False,
                                         ActivePlayerScreen.FONT_COLOR)
            self._screen.get_surface().blit(box_text, self._rect)
