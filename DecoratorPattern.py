# Note that Python doesn't have a built-in abstract class, so we need to use the ABC module to define abstract classes. 
# Also, we don't need to explicitly define interfaces, as in Java. 
# In Python, any class that defines abstract methods can be considered an interface.

from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def get_price(self):
        pass

class HouseBlend(Coffee):
    def get_price(self):
        return 10

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
    
    def get_price(self):
        return self.coffee.get_price()

class Milk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def get_price(self):
        return self.coffee.get_price() + 10

class Sugar(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def get_price(self):
        return self.coffee.get_price() + 20

if __name__ == '__main__':
    coffee_decorator = CoffeeDecorator(HouseBlend())
    print("Normal coffee price:", coffee_decorator.get_price())
    milk_coffee_decorator = Milk(coffee_decorator)
    print("Milk coffee price:", milk_coffee_decorator.get_price())
    sugar_milk_coffee_decorator = Sugar(milk_coffee_decorator)
    print("Sugar milk coffee price:", sugar_milk_coffee_decorator.get_price())
