import unittest
from gilded_rose_solution import GildedRose
from item import Item
from aged_brie import AgedBrie
from sulfuras import Sulfuras
from backstage import BackstagePasses

class GildedRoseTest(unittest.TestCase):
    def test_regular_items(self):
        items = [Item(0,0), Item(5,2),Item(4, 0), Item(0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[1].quality)
        self.assertEqual(4, items[1].sell_in)
        self.assertEqual(0, items[2].quality)
        self.assertEqual(3, items[2].sell_in)
        self.assertEqual(1, items[3].quality)
        self.assertEqual(-1, items[3].sell_in)

    def test_aged_brie(self):
        items = [AgedBrie(0, 0), AgedBrie(5, 2), AgedBrie(4, 50), AgedBrie(-4, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(3, items[1].quality)
        self.assertEqual(4, items[1].sell_in)
        self.assertEqual(50, items[2].quality)
        self.assertEqual(3, items[2].sell_in)
        self.assertEqual(12, items[3].quality)
        self.assertEqual(-5, items[3].sell_in)

    def test_sulfuras(self):
        items = [Sulfuras(3, 1), Sulfuras(33, -3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(-3, items[1].quality)
        self.assertEqual(33, items[1].sell_in)

    def backstage_passes(self):
        items = [BackstagePasses(3, 1), BackstagePasses(33, -3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(3, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()