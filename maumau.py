from enum import Enum
from typing import List


class Suit(Enum):
    Hearts = 1
    Spades = 2
    Diamonds = 3
    Clubs = 4


class Rank(Enum):
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit: Suit = suit
        self.rank: Rank = rank

    def can_be_played_on(self, other: 'Card') -> bool:
        # TODO implement method
        pass

    def __eq__(self, other):
        return isinstance(other, Card) and other.suit == self.suit and other.rank == self.rank

    def __repr__(self) -> str:
        return "({}, {})".format(self.suit, self.rank)


def playable_cards(card: Card, hand: List[Card]) -> List[Card]:
    # TODO implement method
    pass
