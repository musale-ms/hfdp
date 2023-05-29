from abc import ABC, abstractmethod

class Duck(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError

# Swimming, Quacking, Flying vary for the ducks
# Behavior of ducks that is changed
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError

class QuackBehavior(ABC):
    def quack(self):
        raise NotImplementedError

class SwimBehavior(ABC):
    def swim(self):
        raise NotImplementedError

# Implementation of behavior
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("Duck flying with wings")

class FlyWithRocket(FlyBehavior):
    def fly(self):
        print("Duck flying with rocket engine")

# Duck types
class MallardDuck(Duck, FlyWithWings):
    def quack(self):
        print("Mallard duck quack")

    def swim(self):
        print("Mallard duck swim")

    def display(self):
        print("Mallard duck hello")

class RubberDuck(Duck, FlyWithRocket):
    def display(self):
        print("Rubber duck hello")

    def fly(self):
        print("Rubber duck on the No2")


if __name__ == '__main__':
    duck1: Duck = MallardDuck()
    duck2: Duck = RubberDuck()
    print(duck1.fly())
    print(duck2.fly())