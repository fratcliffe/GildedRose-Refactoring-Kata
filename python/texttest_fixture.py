"""
    Output of guilded_rose using test data
"""
from gilded_rose import *
from tabulate import tabulate


if __name__ == "__main__":
    print("OMGHAI!")
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=12, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=40),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=45),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 5
    for day in range(days):
        table = []
        for item in items:
            table.append([item.name, item.sell_in, item.quality])
        print(f"\nDay {day}")
        print(tabulate(
            table,
            headers=["Name", "Sell In", "Quality"],
            tablefmt="pretty",
            colalign=("left", "center", "center")
        ))
        GildedRose(items).update_quality()
