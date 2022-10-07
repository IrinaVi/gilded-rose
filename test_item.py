from item import Item
import unittest

class TestOrder(unittest.TestCase):

    def test_items_update_quality_and_sellin(self):
        items = [Item("foo", 0, 0), Item("chocolate", 5, 2), Item("Bread", 4, 0), Item("Apples", 0, 2), Item("Milk", -2, 2)]
        for item in items:
            item.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(1, items[1].quality)
        self.assertEqual(4, items[1].sell_in)
        self.assertEqual(0, items[2].quality)
        self.assertEqual(3, items[2].sell_in)
        self.assertEqual(1, items[3].quality)
        self.assertEqual(-1, items[3].sell_in)
        self.assertEqual(0, items[4].quality)
        self.assertEqual(-3, items[4].sell_in)

if __name__ == '__main__':
    unittest.main()