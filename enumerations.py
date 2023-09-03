from enum import Enum


class TarneebType(Enum):
    koba = 1
    deenary = 2
    bastawny = 3
    sbeity = 4

class GameState(Enum):
    idle = 0
    started = 1
    terminated = 2
    waiting = 3
    ended = 4

class PlayerState(Enum):
    idle = 0
    waiting = 1
    playing = 2

