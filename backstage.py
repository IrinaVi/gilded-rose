from item import Item

class BackstagePasses(Item):
    def update_quality(self):
        if self.quality <= 50:
            if self.sell_in <= 5:
                self.quality += 3
            elif self.quality <= 10:
                self.quality += 2
            else:
                self.quality += 1
        self.sell_in -= 1