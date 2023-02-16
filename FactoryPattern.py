from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_details(self):
        pass

class Book(Product):
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    
    def get_details(self):
        return f"Book: {self.name} by {self.author}, {self.pages} pages"

class Clothing(Product):
    def __init__(self, name, size, color):
        self.name = name
        self.size = size
        self.color = color
    
    def get_details(self):
        return f"Clothing: {self.name}, size {self.size}, color {self.color}"

class Electronics(Product):
    def __init__(self, name, brand, model):
        self.name = name
        self.brand = brand
        self.model = model
    
    def get_details(self):
        return f"Electronics: {self.name} by {self.brand}, model {self.model}"

class ProductFactory:
    @staticmethod
    def create_product(product_type, *args):
        if product_type == "book":
            return Book(*args)
        elif product_type == "clothing":
            return Clothing(*args)
        elif product_type == "electronics":
            return Electronics(*args)
        else:
            raise ValueError("Invalid product type")

if __name__ == '__main__':
    product1 = ProductFactory.create_product("book", "The Alchemist", "Paulo Coelho", 163)
    product2 = ProductFactory.create_product("clothing", "T-shirt", "M", "Blue")
    product3 = ProductFactory.create_product("electronics", "Laptop", "Dell", "XPS 13")

    print(product1.get_details()) # Output: Book: The Alchemist by Paulo Coelho, 163 pages
    print(product2.get_details()) # Output: Clothing: T-shirt, size M, color Blue
    print(product3.get_details()) # Output: Electronics: Laptop by Dell, model XPS 13
