class Item:
    def __init__(self, sell_in, quality):
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.sell_in, self.quality)

    def update_quality(self):
        if self.quality > 0:
            if self.sell_in < 0:
                self.quality -= 2
            else:
                self.quality -= 1
        self.sell_in -= 1