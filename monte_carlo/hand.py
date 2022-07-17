from enum import Enum
import random

class CardSuit(Enum):
    SPADE    = 1
    HEART    = 2
    CLUBS    = 3
    DIAMONDS = 4

class CardValue(Enum):
    ACE   = 1
    TWO   = 2
    THREE = 3
    FOUR  = 4
    FIVE  = 5
    SIX   = 6
    SEVEN = 7
    EIGHT = 8
    NINE  = 9
    TEN   = 10
    JACK  = 11
    QUEEN = 12
    KING  = 13

class Card:
    def __init__(self, suit: CardSuit, value: CardValue):
        self.suit = suit
        self.value = value

    def __repr__(self):
        pass

class Hand:
    pass

class Board:
    _FLOP_CARDS = 3
    _TURN_CARDS = 1
    _RIVER_CARDS = 1

    def __init__(self):
        self.deck = [
            Card(suit, value)
            for suit in CardSuit
            for value in CardValue
        ]

    def deal_flop(self) -> list[Card]:
        return [self.deal_card() for _ in range(self._FLOP_CARDS)]

    def deal_turn(self):
        return self.deal_card()

    def deal_river(self) -> Card:
        return self.deal_card()

    def deal_card(self) -> Card:
        # Some Random Dealing Algorithm Here
        pass

class HiddenHand:
    pass