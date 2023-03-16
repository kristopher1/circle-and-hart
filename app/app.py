import pygame

from app.game import Game
from app.player import Player
from app.screen.active_player import ActivePlayerScreen
from app.screen.board import Board
from app.screen.player import PlayerScreen
from app.screen.screen import Screen
from event.event_dispatcher import EventDispatcher


class App(object):
    _active_player_screen: ActivePlayerScreen
    _board: Board
    _player2_screen: PlayerScreen
    _player1_screen: PlayerScreen
    _player2: Player
    _player1: Player
    _active_player: Player

    def __init__(self):
        self._running = True
        self._screen = Screen()
        self._dispatcher = EventDispatcher()
        self._board = Board(self._screen, self._dispatcher)
        self._player1 = Player('Fela', 'cat_64.png', 'heart.png')
        self._player2 = Player('Adela', 'dog_64.png', 'circle.png')
        self._game = Game(self._dispatcher, self._board, self._player1, self._player2)

    def init(self):
        self._running = True
        self._screen.init()
        self._board.init()
        self._player1_screen = PlayerScreen(self._screen, self._player1, 20, 20)
        self._player2_screen = PlayerScreen(self._screen, self._player2, -20, 20)
        self._active_player_screen = ActivePlayerScreen(self._screen, self._dispatcher, self._game.get_active_player(),
                                                        170)
        self._active_player_screen.init()
        return True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        self._board.on_event(event)

    def on_loop(self):
        pass

    def on_render(self):
        self._screen.draw()
        self._player1_screen.draw()
        self._player2_screen.draw()
        self._board.draw()
        self._game.draw_marks()
        self._active_player_screen.draw()
        pygame.display.update()
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def execute(self):
        clock = pygame.time.Clock()
        if not self.init():
            self._running = False

        while self._running:
            # This limits the while loop to a max of 60 times per second.
            clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
