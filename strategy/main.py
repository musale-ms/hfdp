from abc import ABC, abstractmethod

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

class AllSwim(SwimBehavior):
    def swim(self):
        print("All ducks swim")

class NaturalQuack(QuackBehavior):
    def quack(self):
        print("Quacking...")

class SqueakQuack(QuackBehavior):
    def quack(self):
        print("Quacking with the help of a battery")

class Duck(ABC):
    quack: QuackBehavior
    swim: SwimBehavior
    fly: FlyBehavior

    def setQuack(self, qb: QuackBehavior):
        self.quack = qb

    def performQuack(self):
        self.quack.quack()

    def setSwim(self, sb: SwimBehavior):
        self.swim = sb

    def performSwim(self):
        self.swim.swim()

    def setFly(self, fb: FlyBehavior):
        self.fly = fb

    def performFly(self):
        self.fly.fly()

    @abstractmethod
    def display(self):
        raise NotImplementedError


# Duck types
class MallardDuck(Duck):

    def __init__(self):
        super().__init__()
        self.fly = FlyWithWings()
        self.swim = AllSwim()
        self.quack = NaturalQuack()

    def quack(self):
        print("Mallard duck quack")

    def swim(self):
        print("Mallard duck swim")

    def display(self):
        print("Mallard duck hello")

class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly = FlyWithRocket()
        self.swim = AllSwim()
        self.quack = SqueakQuack()

    def display(self):
        print("Rubber duck hello")

    def fly(self):
        print("Rubber duck on the No2")


if __name__ == '__main__':
    duck1: Duck = MallardDuck()
    duck2: Duck = RubberDuck()
    duck1.performFly()
    duck2.performFly()
    duck2.performQuack()
    print("Rocket powered Mallard set dynamically")
    duck1.setFly(FlyWithRocket())
    duck1.performFly()