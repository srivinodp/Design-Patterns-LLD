import random
from abc import ABC, abstractmethod


#Note - 
# This Python code defines the Observer and Observable interfaces as abstract classes using the abc module. The Item class and ShoppingCart class are defined in a similar way to the Java implementation.

# The main differences in the Python code are that we use the @abstractmethod decorator to define abstract methods in the Observer and Observable classes, and we use the __str__() method instead of toString() to print the Item object
class Observer(ABC):
    @abstractmethod
    def update(self, observable):
        pass

class Observable(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

    @abstractmethod
    def print_items(self):
        pass

class Item:
    def __init__(self):
        self.id = random.randint(0, int(1e5))

    def get_price(self):
        return 0

    def __str__(self):
        return str(self.id)

class ShoppingCart(Observable):
    def __init__(self):
        self.items = []
        self.observers = []

    def add_item(self, item):
        self.items.append(item)
        self.notify_observers()

    def remove_item(self, item):
        self.items.remove(item)
        self.notify_observers()

    def get_total_price(self):
        total_price = 0.0
        for item in self.items:
            total_price += item.get_price()
        return total_price

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)
        self.print_items()
        print("--------------")

    def print_items(self):
        for item in self.items:
            print(item)

if __name__ == '__main__':
    s_cart = ShoppingCart()
    for i in range(5):
        s_cart.add_item(Item())
