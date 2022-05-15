from typing import List
class Counter:
    id: str
    _items: dict()  # <- suggested, you can change this
    counter = 0
    price_counter = 0.0

    def __init__(self, ID: str):
        '''creates a new counter with a given ID'''
        self.id = ID
        self._items = dict()
        self.counter = 0
        self.price_counter = 0

    def add(self, item_name: str, amount: int, price_of_unit: float) -> None:
        '''Adds amount of items with item_name and specifies price_of_unit. You can assume that every addition for the same item_name will have the same price_of_unit.'''
        self.counter += amount
        self.price_counter += (amount * price_of_unit)
        self._items[self.id] = [self.counter, self.price_counter]
        print(self._items)

    def remove(self, item_name: str, amount: int) -> None:
        '''Removes the given amount of items with the given item name.'''

    def reset(self):
        '''Removes all the records of items previously added.'''

    def get_total(self) -> float:
        '''Returns the total sum rounded to two digits after decimal point .'''

    def status(self) -> str:
        '''Returs string of form "Id N M", where Id is id of counter, N is total amount of all items and M total price of them rounded to two digits after decimal point (with both digits printed).'''
        ans = ''
        for key, values in self._items.items():
            ans += key + " "
            for value in values:
                if type(value) == int:
                    ans += str(value) + " "
                else:
                    ans += "{:.2f}".format(value)
        print(ans)
        return ans

c = Counter("C001")
assert c.id == "C001"   #test_1
c.add("Spaghetti", 5, 1.80)
assert c.status()=="C001 5 9.00"   #test_2
c.add("Ice Cream", 2, 3.4)
assert c.status()=="C001 7 15.80"   #test_3
assert abs(c.get_total()-15.8)<0.0001   #test_4
c.add("Spaghetti", 3, 1.8)
assert c.status()=="C001 10 21.20"   #test_5
c.remove("Ice Cream", 1)
assert c.status()=="C001 9 17.80"   #test_6
c.reset()
c.add("Coke", 5, 1.45)
assert c.status()== "C001 5 7.25"   #test_7