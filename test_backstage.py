from backstage import BackstagePasses
import unittest

class BackstagePasses(unittest.TestCase):
    def backstage_passes_updates_test(self):
        items = [BackstagePasses("Backstage passes", 20, 23), BackstagePasses("Backstage passes", 10, 2), BackstagePasses("Backstage passes", 7, 0), BackstagePasses("Backstage passes", 5, 9), BackstagePasses("Backstage passes", 1, 5)]
        for item in items:
            item.update_quality()
        self.assertEqual(24, items[0].quality)
        self.assertEqual(19, items[0].sell_in)
        self.assertEqual(4, items[1].quality)
        self.assertEqual(9, items[1].sell_in)
        self.assertEqual(2, items[2].quality)
        self.assertEqual(6, items[2].sell_in)
        self.assertEqual(12, items[3].quality)
        self.assertEqual(4, items[3].sell_in)
        self.assertEqual(8, items[4].quality)
        self.assertEqual(2, items[4].sell_in)

if __name__ == '__main__':
    unittest.main()
