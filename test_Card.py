from unittest import TestCase
from Card import Card
class test_Card(TestCase):

    def setUp(self):
        self.card=Card(13, "Diamond")
        self.card2=Card(12, "Spade")

    def tearDown(self):
        pass

    def test_is_bigger(self):
        self.assertEqual(self.card.isBigger(self.card2),"King of Diamonds is the bigger card.")

        self.card.value=11
        self.assertEqual(self.card.isBigger(self.card2),"Queen of Spades is the bigger card.")

        self.card.value=12
        self.assertEqual(self.card.isBigger(self.card2),"Queen of Spades is the bigger card.")

        self.card.shape="Diamond"
        self.card2.shape="Club"
        print(self.card)
        self.assertEqual(self.card2.isBigger(self.card),"Queen of Clubs is the bigger card.")

        self.card2.shape="Diamond"
        self.card.shape="Club"
        print(self.card)
        self.assertEqual(self.card2.isBigger(self.card),"Queen of Clubs is the bigger card.")
