import random

if __name__ == "__main__":
    # Write your solution here
    pass

class Car:
    def __init__(self, engine: str, weight: (int, float), colour: str):
        self.engine = engine
        self.weight = weight
        self.colour = colour
        """Базовый класс "машина".
        :param engine: Тип двигателя авто
        :param weight: Снаряженная масса авто
        :param colour: Цвет авто
        """
    @property
    def engine(self):
        return self._engine
    @property
    def weight(self):
        return self._weight
    @property
    def colour(self):
        return self._colour

    @engine.setter
    def engine(self, str):
        self._engine = str
    @weight.setter
    def weight(self, int):
        self._weight = int
    @colour.setter
    def colour(self, str):
        self._colour = str

    def __repr__(self):
        return f"{self.__class__.__name__}(engine={self.engine!r}, weight={self.weight!r}, colour={self.colour!r})"

    def __str__(self):
        return f"Двигатель {self.engine}. Вес {self.weight}. Цвет {self.colour}"

    def changecolour(self):
        colorlist = ['black', 'white', 'blue', 'green', 'yellow', 'red']  # список цветов
        newcolour = random.choice(colorlist)
        self.colour = newcolour
        return self.colour

class Drive(Car):
    def __init__(self, engine: str, weight: (int, float), colour: str, wheel_drive: str):
        super().__init__(engine, weight, colour)
        self.engine = engine
        self.weight = weight
        self.colour = colour
        self.drive = None
        """Дочерний класс "Приводная(машина)".
        :param engine: Тип двигателя авто
        :param weight: Снаряженная масса авто
        :param colour: Цвет авто
        :param wheel_drive: Привод авто
        """
    @property
    def engine(self):
        return self._engine
    @property
    def weight(self):
        return self._weight
    @property
    def colour(self):
        return self._colour
    @property
    def drive(self):
        return self._drive

    @engine.setter
    def engine(self, str):
        self._engine = str
    @weight.setter
    def weight(self, int):
        self._weight = int
    @colour.setter
    def colour(self, str):
        self._colour = str
    @drive.setter
    def drive(self, str):
        self._drive = str
    def selectyarn(self):
        self.drive = random.choice(['AWD', 'RWD', 'FWD']) #привод авто
        return self.drive

    def __str__(self):
        return f"Двигатель {self.engine}. Вес {self.weight}. Цвет {self.colour}. Привод {self.drive}"


first = Car("electro", 1, "white")
first.changecolour()
print(first)

second = Drive("diesel", 3, "black", "AWD")
second.selectyarn()
print(second)
