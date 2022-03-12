"""
    Program to manage inventory
"""


class GildedRose(object):
    """
        Class which takes a list of items for which attributes should be updated
    """
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """
            Function to update attributes of an item based on criteria
        """
        for item in self.items:
            if not any(x in item.name for x in ["Backstage passes", "Aged Brie"]):
                if item.quality > 0:
                    if not any(x in item.name for x in ["Sulfuras", "Conjured"]):
                        item.quality -= 1
                    elif "Conjured" in item.name:
                        if item.quality == 1:
                            item.quality -= 1
                        else:
                            item.quality -= 2
            elif item.quality < 50:
                item.quality += 1
                if "Backstage passes" in item.name:
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality += 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality += 1
            if "Sulfuras" not in item.name:
                item.sell_in -= 1
            if item.sell_in < 0:
                if not any(x in item.name for x in ["Backstage passes", "Aged Brie"]):
                    if item.quality > 0:
                        if "Sulfuras" not in item.name:
                            item.quality -= 1
                elif "Backstage passes" in item.name:
                    item.quality -= item.quality
                elif item.quality < 50:
                    item.quality += 1


class Item:
    """
        Class for assigning attributes to each item
    """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
