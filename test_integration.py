# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_regular_items(self):
        items = [Item("foo", 0, 0), Item("chocolate", 5, 2), Item("Bread", 4, 0), Item("Apples", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[1].quality)
        self.assertEqual(4, items[1].sell_in)
        self.assertEqual(0, items[2].quality)
        self.assertEqual(3, items[2].sell_in)
        self.assertEqual(0, items[3].quality)
        self.assertEqual(-1, items[3].sell_in)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 0, 0), Item("Aged Brie", 5, 2), Item("Aged Brie", 4, 50), Item("Aged Brie", -4, 10)]
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
        items = [Item("Sulfuras, Hand of Ragnaros", 3, 1), Item("Sulfuras, Hand of Ragnaros", 33, -3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(3, items[0].sell_in)
        self.assertEqual(-3, items[1].quality)
        self.assertEqual(33, items[1].sell_in)

    def test_sulfuras(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 3, 1), Item("Backstage passes to a TAFKAL80ETC concert", 33, -3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(3, items[0].sell_in)

if __name__ == '__main__':
    unittest.main()