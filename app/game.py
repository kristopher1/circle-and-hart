from app.screen.board import Board
from app.game_event import GameEvent
from app.player import Player
from event.event import Event
from event.event_dispatcher import EventDispatcher


class Game(object):
    WIN_TUPLES = (
        # vertical lines
        ((1, 1), (1, 2), (1, 3)),
        ((2, 1), (2, 2), (2, 3)),
        ((3, 1), (3, 2), (3, 3)),
        # horizontal lines
        ((1, 1), (2, 1), (3, 1)),
        ((1, 2), (2, 2), (3, 2)),
        ((1, 3), (2, 3), (3, 3)),
        # diagonal lines
        ((1, 1), (2, 2), (3, 3)),
        ((1, 3), (2, 2), (3, 1)),
    )

    def __init__(self, event_dispatcher: EventDispatcher, board: Board, player1: Player, player2: Player):
        self._event_dispatcher = event_dispatcher
        self._event_dispatcher.add_event_listener(GameEvent.BOARD_SQUARE_CLICKED, self.on_board_square_clicked)
        self._board = board
        self._player1 = player1
        self._player2 = player2
        self._active_player = self._player1
        self._event_dispatcher.dispatch_event(GameEvent(GameEvent.ACTIVE_PLAYER_SET, self._player1))
        self._board_data = {}

    def get_active_player(self):
        return self._active_player

    def on_board_square_clicked(self, event: Event):
        (x, y) = event.data
        if self._mark_square(x, y):
            self._board.draw_on_field(x, y, self._active_player.get_mark())
            if self._player_win_check():
                return self.on_win()
            self._switch_active_player()
        if sum(len(v) for v in self._board_data.values()) == 9:
            self._board_data = {}
            self._event_dispatcher.dispatch_event(GameEvent(GameEvent.GAME_NOT_CONCLUDED))

    def on_win(self):
        self._active_player.incr_score()
        self._switch_active_player()
        self._board_data = {}
        self._event_dispatcher.dispatch_event(GameEvent(GameEvent.PLAYER_WIN, self._active_player))

    def draw_marks(self):
        for x in self._board_data:
            for y in self._board_data.get(x, {}):
                self._board.draw_on_field(x, y, self._board_data[x][y].get_mark())

    def _mark_square(self, x: int, y: int):
        if self._board_data.get(x, {}).get(y):
            return False
        self._board_data.setdefault(x, {})[y] = self._active_player
        return True

    def _switch_active_player(self):
        if self._active_player == self._player1:
            self._active_player = self._player2
        else:
            self._active_player = self._player1
        self._event_dispatcher.dispatch_event(GameEvent(GameEvent.ACTIVE_PLAYER_SET, self._active_player))

    def _player_win_check(self):
        for lines in self.WIN_TUPLES:
            win = True
            for sets in lines:
                (x, y) = sets
                if self._board_data.get(x, {}).get(y) != self._active_player:
                    win = False
            if win:
                return True

        return False
