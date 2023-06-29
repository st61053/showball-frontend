from typing import TypedDict


class PlayerStats(TypedDict):
    points: int
    coins: int
    strike: int


class PlayerTokenStats(TypedDict):
    count: int
    upgrade: int
    straight: bool


class Player(TypedDict):
    player_id: str
    name: str
    password: str
    stats: PlayerStats
    tokens: dict[str, PlayerTokenStats]


class Token(TypedDict):
    token_id: str
    name: str
    points: dict[int, int]
    coins: dict[int, int]
    upgrades: dict[int, int]


class PlayerStrike(TypedDict):
    player_id: int
    token_id: int
    amount: int
    points: int
    coins: int
