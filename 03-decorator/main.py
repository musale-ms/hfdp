"""
Decorator pattern: attaches additional responsibilites to an object dynamically.
"""

from abc import abstractmethod, ABC


class Beverage(ABC):
    """
    The abstract component.
    """

    description: str

    def get_description(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError


class CondimentDecorator(Beverage):
    """
    The abstract condiment decorator.
    """

    beverage: Beverage

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError


class Espresso(Beverage):
    """
    Concrete component Espresso.
    """

    def __init__(self) -> None:
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self) -> None:
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def __init__(self) -> None:
        self.description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99


class Decaf(Beverage):
    def __init__(self) -> None:
        self.description = "Decaf Coffee"

    def cost(self) -> float:
        return 1.05


class Mocha(CondimentDecorator):
    """
    Mocha condiment.
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def get_description(self) -> str:
        return f"{self.beverage.get_description()}, Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20


class Soy(CondimentDecorator):
    """
    Soy condiment.
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def get_description(self) -> str:
        return f"{self.beverage.get_description()}, Soy"

    def cost(self) -> float:
        return self.beverage.cost() + 0.15


class Whip(CondimentDecorator):
    """
    Whip condiment.
    """

    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def get_description(self) -> str:
        return f"{self.beverage.get_description()}, Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10


if __name__ == "__main__":
    # Espresso with no condiments
    beverage: Beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")

    # Double mocha soy latte with whip
    # Combine HouseBlend, Soy, 2 shots of Mocha and Whip
    beverage_2: Beverage = HouseBlend()
    beverage_2 = Soy(beverage_2)
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Mocha(beverage_2)
    beverage_2 = Whip(beverage_2)
    print(f"{beverage_2.get_description()} ${beverage_2.cost()}")
