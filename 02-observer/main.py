from abc import ABC, abstractmethod
from typing import List
import time


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        raise NotImplemented

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError


class Subject(ABC):
    @abstractmethod
    def registerObserver(self, o: Observer):
        raise NotImplemented

    @abstractmethod
    def removeObserver(self, o: Observer):
        raise NotImplemented

    @abstractmethod
    def notifyObservers(self):
        raise NotImplemented


class WeatherData(Subject):
    observers: List[Observer]
    temperature: float
    humidity: float
    pressure: float

    def __init__(self) -> None:
        super().__init__()
        self.observers = []

    def registerObserver(self, o: Observer):
        self.observers.append(o)

    def removeObserver(self, o: Observer):
        self.observers.remove(o)

    def notifyObservers(self):
        print(f"current observers {self.observers}")
        for o in self.observers:
            o.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure


class CurrentConditionsDisplay(DisplayElement, Observer):
    temperature: float
    humidity: float
    pressure: float
    weather_data: WeatherData

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.registerObserver(self)

    def display(self):
        temp = f"Current Temp: {self.temperature} Celsius"
        humidity = f"Current Humidity: {self.humidity} Celsius"
        pressure = f"Current Pressure: {self.pressure} Celsius"

        print("=== CURRENT CONDITIONS ===")
        print(temp, humidity, pressure, sep="\n")
        print("=== END OF DISPLAY ===")

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure

        self.display()


class HeatIndexDisplay(DisplayElement, Observer):
    temperature: float
    humidity: float
    pressure: float
    weather_data: WeatherData

    def __init__(self, weather_data: WeatherData) -> None:
        self.weather_data = weather_data
        self.weather_data.registerObserver(self)

    def display(self):
        value = (self.temperature * self.humidity) / self.humidity
        heat_index = f"Heat Index: {value} Musales"

        print("=== HEAT INDEX ===")
        print(heat_index, sep="\n")
        print("=== END OF DISPLAY ===")

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure

        self.display()


if __name__ == "__main__":
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data=weather_data)
    hi_display = HeatIndexDisplay(weather_data=weather_data)

    weather_data.setMeasurements(80, 24, 12)
    weather_data.notifyObservers()
    time.sleep(5)

    weather_data.setMeasurements(74, 14, 34)
    weather_data.notifyObservers()
    time.sleep(5)

    weather_data.setMeasurements(56, 53, 13)
    weather_data.notifyObservers()
    time.sleep(5)

    weather_data.setMeasurements(34, 24, 54)
    weather_data.notifyObservers()
    time.sleep(5)
