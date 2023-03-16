from math import floor

import pygame
from pygame import Surface, SurfaceType
from pygame.rect import RectType

from app.game_event import GameEvent
from app.screen.screen import Screen
from event.event_dispatcher import EventDispatcher


#      xv1     xh1     xh2     xv2
# yh1           x       x
#               |       |
#         1-1   |  1-2  |  1-3
#               |       |
# yv2   x-------x-------x-------x
#               |       |
#         2-1   |  2-2  |  2-3
#               |       |
# yv1   x-------x-------x-------x
#               |       |
#         3-1   |  3-2  |  3-3
#               |       |
# yh2           x       x
#

class Board(object):
    _screen: Screen
    _bord_rect: RectType
    _bord_fields_rect: dict
    _xv1: int
    _xh1: int
    _xh2: int
    _xv2: int
    _yh1: int
    _yv2: int
    _yv1: int
    _yh2: int

    def __init__(self, screen: Screen, event_dispatcher: EventDispatcher):
        self._screen = screen
        self._event_dispatcher = event_dispatcher
        self._line_weight = 5
        self._line_width = 450
        self._bottom_distance = 30
        self._line_color = "white"

    def init(self):
        self._calculate_points()
        self._create_rects()
        self.draw()

    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self._bord_rect.collidepoint(pygame.mouse.get_pos()):
                self._event_dispatcher.dispatch_event(GameEvent(GameEvent.BOARD_CLICKED))
                self._click_board_event()

    def draw_on_field(self, x: int, y: int, img: Surface):
        rect: RectType = self._bord_fields_rect[x][y]
        cord_fix = ((self._line_width / 3) - img.get_width()) / 2
        self._screen.get_surface().blit(img, (rect.x + cord_fix, rect.y + cord_fix))

    def draw(self):
        # vertical lines
        surface = self._screen.get_surface()
        pygame.draw.line(surface, self._line_color, (self._xh1, self._yh2), (self._xh1, self._yh1),
                         self._line_weight)
        pygame.draw.line(surface, self._line_color, (self._xh2, self._yh2), (self._xh2, self._yh1),
                         self._line_weight)
        # horizontal line
        pygame.draw.line(surface, self._line_color, (self._xv1, self._yv1), (self._xv2, self._yv1),
                         self._line_weight)
        pygame.draw.line(surface, self._line_color, (self._xv1, self._yv2), (self._xv2, self._yv2),
                         self._line_weight)

    def _click_board_event(self):
        for x in self._bord_fields_rect:
            for y in self._bord_fields_rect[x]:
                if self._bord_fields_rect[x][y].collidepoint(pygame.mouse.get_pos()):
                    self._event_dispatcher.dispatch_event(GameEvent(GameEvent.BOARD_SQUARE_CLICKED, (x, y)))

    def _calculate_points(self):
        # vertical line points
        self._xh1 = floor((self._screen.get_width() / 2) - (self._line_width / 6))
        self._xh2 = floor((self._screen.get_width() / 2) + (self._line_width / 6))
        self._yh2 = self._screen.get_height() - self._bottom_distance
        self._yh1 = self._yh2 - self._line_width
        # horizontal line points
        self._xv1 = floor((self._screen.get_width() - self._line_width) / 2)
        self._xv2 = self._screen.get_width() - self._xv1
        self._yv1 = floor(self._screen.get_height() - self._bottom_distance - (self._line_width / 3))
        self._yv2 = floor(self._yv1 - (self._line_width / 3))

    def _create_rects(self):
        # board rect space
        self._bord_rect = pygame.Rect(self._xv1, self._yh1, self._line_width, self._line_width)
        square_width = floor(self._line_width / 3)
        square_points = [
            [[self._xv1, self._yh1], [self._xh1, self._yh1], [self._xh2, self._yh1]],
            [[self._xv1, self._yv2], [self._xh1, self._yv2], [self._xh2, self._yv2]],
            [[self._xv1, self._yv1], [self._xh1, self._yv1], [self._xh2, self._yv1]],
        ]
        self._bord_fields_rect = {}
        for x, points in enumerate(square_points):
            for y, point in enumerate(points):
                self._bord_fields_rect.setdefault(x + 1, {})[y + 1] = pygame.Rect(point[0], point[1], square_width,
                                                                                  square_width)
