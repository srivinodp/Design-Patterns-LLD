interface Coffee{
    public int getPrice();
}
class HouseBlend implements Coffee{
    @Override
    public int getPrice(){
        return 10;
    }
}
class CoffeeDecorator implements Coffee{
    Coffee coffee;
    CoffeeDecorator(Coffee coffee){
        this.coffee = coffee;
    }
    public int getPrice(){
        return this.coffee.getPrice();
    }
}
class Milk extends CoffeeDecorator{
    Milk(Coffee coffee){
        super(coffee);
    }
    public int getPrice(){
        return coffee.getPrice()+10;
    }
}
class Sugar extends CoffeeDecorator{
    Sugar(Coffee coffee){
        super(coffee);
    }
    public int getPrice(){
        return coffee.getPrice()+20;
    }
}
public class DecoratorPattern {
    public static void main(String[] args) {
        CoffeeDecorator coffeeDecorator = new CoffeeDecorator(new HouseBlend());
        System.out.println("Normal coffee price : "+coffeeDecorator.getPrice());
        Milk milkCoffeeDecorator = new Milk(coffeeDecorator);
        System.out.println("milk coffee price : "+milkCoffeeDecorator.getPrice());
        Sugar sugarMilkCoffeeDecorator = new Sugar(milkCoffeeDecorator);
        System.out.println("sugar milk coffee price : "+sugarMilkCoffeeDecorator.getPrice());
        
    }
    
    
}
