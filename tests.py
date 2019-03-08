import unittest
from maumau import Card, Suit, Rank, playable_cards


class MauMauTest(unittest.TestCase):
    def test_can_be_played(self):
        self.assertTrue(Card(Suit.Hearts, Rank.Seven).can_be_played_on(Card(Suit.Hearts, Rank.Seven)))
        self.assertTrue(Card(Suit.Diamonds, Rank.Nine).can_be_played_on(Card(Suit.Diamonds, Rank.Jack)))
        self.assertTrue(Card(Suit.Hearts, Rank.Eight).can_be_played_on(Card(Suit.Diamonds, Rank.Eight)))

        self.assertFalse(Card(Suit.Hearts, Rank.Jack).can_be_played_on(Card(Suit.Clubs, Rank.Queen)))
        self.assertFalse(Card(Suit.Diamonds, Rank.Seven).can_be_played_on(Card(Suit.Spades, Rank.Ace)))
        self.assertFalse(Card(Suit.Hearts, Rank.King).can_be_played_on(Card(Suit.Spades, Rank.Eight)))

    def test_playable_cards(self):
        self.assertEqual([], playable_cards(Card(Suit.Hearts, Rank.Seven), []))
        self.assertEqual([Card(Suit.Diamonds, Rank.Queen), Card(Suit.Hearts, Rank.King)],
                         playable_cards(Card(Suit.Diamonds, Rank.King),
                                        [Card(Suit.Diamonds, Rank.Queen), Card(Suit.Hearts, Rank.King)]))
        self.assertEqual([Card(Suit.Spades, Rank.Seven), Card(Suit.Diamonds, Rank.Nine)],
                         playable_cards(Card(Suit.Spades, Rank.Nine),
                                        [Card(Suit.Diamonds, Rank.Seven), Card(Suit.Hearts, Rank.Eight),
                                         Card(Suit.Spades, Rank.Seven), Card(Suit.Hearts, Rank.Ace),
                                         Card(Suit.Diamonds, Rank.Nine)]))


if __name__ == '__main__':
    unittest.main()
