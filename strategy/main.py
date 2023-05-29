from abc import ABC, abstractmethod

class Duck(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplementedError

    @abstractmethod
    def swim(self):
        raise NotImplementedError

    @abstractmethod
    def display(self):
        raise NotImplementedError

class MallardDuck(Duck):
    def quack(self):
        print("Mallard duck quack")

    def swim(self):
        print("Mallard duck swim")

    def display(self):
        print("Mallard duck hello")


if __name__ == '__main__':
    mallard = MallardDuck()
    print(mallard.swim())