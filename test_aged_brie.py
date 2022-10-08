import unittest
from aged_brie import AgedBrie

class AgedBrieTest(unittest.TestCase):

    def test_aged_brie(self):
        items = [AgedBrie(0, 0), AgedBrie(5, 2), AgedBrie(4, 50), AgedBrie(-4, 10)]
        for item in items:
            item.update_quality()
        self.assertEqual(2, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(3, items[1].quality)
        self.assertEqual(4, items[1].sell_in)
        self.assertEqual(50, items[2].quality)
        self.assertEqual(3, items[2].sell_in)
        self.assertEqual(12, items[3].quality)
        self.assertEqual(-5, items[3].sell_in)

if __name__ == '__main__':
    unittest.main()