from item import Item

#increases in quality the older it gets
class AgedBrie(Item):
    def update_quality(self):
        if self.quality < 50 and self.sell_in > 0:
            self.quality += 1
        elif self.sell_in <= 0:
                self.quality += 2
        self.sell_in -= 1