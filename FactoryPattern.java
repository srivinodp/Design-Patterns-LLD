// In this example, the ProductFactory class allows us to create objects of the Product classes without exposing the creation logic to the client. 
// This makes the code more modular and easier to maintain, as we can add new types of products without changing the client code. 
// The client only needs to know the type of the product it wants to create and the ProductFactory takes care of the rest.

interface Product {
    String getDescription();
}
class Book implements Product {
    @Override
    public String getDescription() {
        return "This is a book";
    }
}

class Clothing implements Product {
    @Override
    public String getDescription() {
        return "This is a piece of clothing";
    }
}

class Electronics implements Product {
    @Override
    public String getDescription() {
        return "This is an electronic item";
    }
}

class ProductFactory {
    public Product createProduct(String type) {
        if (type.equals("book")) {
            return new Book();
        } else if (type.equals("clothing")) {
            return new Clothing();
        } else if (type.equals("electronics")) {
            return new Electronics();
        } else {
            return null;
        }
    }
}

public class FactoryPattern{
    public static void main(String[] args) {
        ProductFactory factory = new ProductFactory();
        Product book = factory.createProduct("book");
        Product clothing = factory.createProduct("clothing");
        Product electronics = factory.createProduct("electronics");

        System.out.println(book.getDescription());
        System.out.println(clothing.getDescription());
        System.out.println(electronics.getDescription());
    }
}