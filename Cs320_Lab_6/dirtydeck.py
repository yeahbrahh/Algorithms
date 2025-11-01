from playingcard import PlayingCard, CardSuit, _valid_rank_, _convert_to_rank
from collections.abc import Container
import unittest
import random


_full_deck_ = [PlayingCard(s, r) for s in CardSuit for r in range(1, 14)]


class DirtyDeck(Container):

    def __init__(self, *, hide=None):
        self.deck = _full_deck_.copy()
        self.hidden = None
        if hide is not None:
            if not _valid_rank_(hide):
                raise ValueError(f"{hide} is not a card rank")
            self.hidden = _convert_to_rank(hide)

    def __str__(self):
        retstr = ""
        for c in self.deck:
            retstr += f"{str(c)} "
        return retstr

    def __contains__(self, c):
        return c in self.deck

    def __len__(self):
        return len(self.deck)

    def __iter__(self):
        return iter(self.deck)

# -- To shuffle an array a of n elements (indices 0..n − 1):

# for i from n − 1 down to 1 do
#      j ← random integer such that 0 ≤ j ≤ i
#      exchange a[j] and a[i]

    def shuffle(self):
        for i in range(self.__len__() - 1, 0, -1):
            j = random.randint(0, i)
            self.deck[j], self.deck[i] = self.deck[i], self.deck[j]
        if self.hidden is not None:
            for card in self.deck[:]:
                if card.rank == self.hidden:
                    self.deck.remove(card)
                    self.deck.append(card)

    def deal(self):
        if self.__len__() <= 13:
            raise ResourceWarning("low deck")

        return self.deck.pop(0)


# dirt = DirtyDeck(hide=3)
# print(dirt.shuffle())


if __name__ == "__main__":

    d = DirtyDeck()  # rework as unittests
    print(d)
    print(f"len={len(d)}")

    for rank in [10, "Jack", "Queen", "King", "Ace", "Joker", 2]:
        _ = DirtyDeck(hide=rank)

    try:
        _ = DirtyDeck(hide=15)
    except Exception:
        print("invalid hide fails")
