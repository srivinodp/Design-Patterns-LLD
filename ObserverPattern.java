


import java.util.*;

interface Observer {
    void update(int value);
}

interface Observable {
    void addObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers();
}

class Data implements Observable {
    private int value;
    private List<Observer> observers = new ArrayList<Observer>();
    
    public int getValue() {
        return value;
    }
    
    public void setValue(int value) {
        this.value = value;
        notifyObservers();
    }
    
    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }
    
    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }
    s
    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(value);
        }
    }
}

class DataObserver implements Observer {
    @Override
    public void update(int value) {
        System.out.println("Value updated: " + value);
    }
}

public class ObserverPattern {
    public static void main(String[] args) {
        Data data = new Data();
        
        DataObserver observer = new DataObserver();
        data.addObserver(observer);
        data.setValue(10);
        data.setValue(20);
    }
}
