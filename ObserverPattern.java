import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.random.RandomGenerator;

interface Observer {
    void update(Observable observable);
}

interface Observable {
    void addObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers();
    void printItems();
}
class Item{
    int id;
    Item(){Random rand = new Random();this.id = rand.nextInt((int)1e5);}
    int getPrice(){return 0;}
    @Override
    public String toString(){
        return ""+this.id;
    }
}

class ShoppingCart implements Observable {
    
    private List<Item> items;
    private List<Observer> observers;

    public ShoppingCart() {
        this.items = new ArrayList<>();
        this.observers = new ArrayList<>();
    }

    public void addItem(Item item) {
        items.add(item);
        notifyObservers();
    }

    public void removeItem(Item item) {
        items.remove(item);
        notifyObservers();
    }

    public double getTotalPrice() {
        double totalPrice = 0.0;
        for (Item item : items) {
            totalPrice += item.getPrice();
        }
        return totalPrice;
    }

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(this);
        }
        printItems();
        System.out.println("--------------");
    }
    @Override
    public void printItems(){
        for(Item it:items){
            System.out.println(it);
        }
    }
    
}
public class ObserverPattern{
    public static void main(String[] args) {
        ShoppingCart sCart = new ShoppingCart();
        for(int i = 0;i<5;i++) sCart.addItem(new Item());
    }
}
