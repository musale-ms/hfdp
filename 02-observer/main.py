from abc import ABC, abstractmethod
from typing import List
import time
import random


class Observer(ABC):
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        raise NotImplemented

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"


class Observer2(ABC):
    @abstractmethod
    def update(self):
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


class WeatherData2(Subject):
    def __init__(self) -> None:
        self._observers: List[Observer] = []
        self._temperature: float = 0.0
        self._humidity: float = 0.0
        self._pressure: float = 0.0

    @property
    def observers(self):
        return self._observers

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        self._pressure = value

    def registerObserver(self, o: Observer):
        self.observers.append(o)

    def removeObserver(self, o: Observer):
        self.observers.remove(o)

    def notifyObservers(self):
        print(f"current observers {self.observers}")
        for o in self.observers:
            o.update()

    def measurementsChanged(self):
        self.notifyObservers()


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


class ForecastDisplay(DisplayElement, Observer2):
    def __init__(self, weather_data: WeatherData2) -> None:
        self.weather_data: WeatherData2 = weather_data
        self.weather_data.registerObserver(self)

    def display(self):
        temp = f"Temperature at: {self.temperature}o Celsius"
        humidity = f"Humidity is: {self.humidity} Musales"
        pressure = f"Pressure at: {self.pressure}"

        print("=== WEATHER FORECAST ===")
        print(temp, humidity, pressure, sep="\n")
        print("=== END OF DISPLAY ===")

    def update(self):
        self.temperature = self.weather_data.temperature
        self.humidity = self.weather_data.humidity
        self.pressure = self.weather_data.pressure

        self.display()


if __name__ == "__main__":
    weather_data = WeatherData()
    current_display = CurrentConditionsDisplay(weather_data=weather_data)
    hi_display = HeatIndexDisplay(weather_data=weather_data)

    while True:
        weather_data.setMeasurements(
            random.uniform(-50.0, 50),
            random.uniform(-100.0, 100.0),
            random.uniform(-40.0, 40.0),
        )
        weather_data.notifyObservers()
        time.sleep(3)

    # weather_data = WeatherData2()
    # forecast_display = ForecastDisplay(weather_data=weather_data)

    # while True:
    #     weather_data.temperature = random.uniform(-50.0, 50)
    #     weather_data.humidity = random.uniform(-100.0, 100.0)
    #     weather_data.pressure = random.uniform(-40.0, 40.0)
    #     weather_data.notifyObservers()
    #     time.sleep(3)
