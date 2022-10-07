import unittest
from sulfuras import Sulfuras

class SulfurasTest(unittest.TestCase):
    def test_sulfuras(self):
        items = [Sulfuras("Sulfuras, Hand of Ragnaros", 3, 1), Sulfuras("Sulfuras, Hand of Ragnaros", -33, 0)]
        for item in items:
            item.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(0, items[1].quality)
        self.assertEqual(-33, items[1].sell_in)

if __name__ == '__main__':
    unittest.main()