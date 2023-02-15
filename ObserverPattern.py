class Observer:
    def update(self, value):
        pass

class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, value):
        for observer in self.observers:
            observer.update(value)

class Data(Observable):
    def __init__(self):
        super().__init__()
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.notify_observers(value)

class DataObserver(Observer):
    def update(self, value):
        print(f"Value updated: {value}")

data = Data()
observer = DataObserver()
data.add_observer(observer)
data.value = 10
data.value = 20
