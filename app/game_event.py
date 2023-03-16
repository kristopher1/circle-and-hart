from event.event import Event


class GameEvent(Event):
    """
    When subclassing Event class the only thing you must do is to define
    a list of class level constants which defines the event types and the
    string associated to them
    """

    BOARD_CLICKED = "BOARD_CLICKED"
    BOARD_SQUARE_CLICKED = "BOARD_SQUARE_CLICKED"
    ACTIVE_PLAYER_SET = "ACTIVE_PLAYER_SET"
    GAME_NOT_CONCLUDED = "GAME_NOT_CONCLUDED"
    PLAYER_WIN = "PLAYER_WIN"
