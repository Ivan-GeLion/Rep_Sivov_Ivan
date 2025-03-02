if __name__ == "__main__":
    # Write your solution here
    pass

import random


class car:
    def __init__(self, engine: str, weight: (int, float), colour: str):
        self.engine = None
        self.weight = None
        self.colour = None
        """Базовый класс "машина".
        :param engine: Тип двигателя авто
        :param weight: Снаряженная масса авто
        :param colour: Цвет авто
        """

    def set_params(self, engine: str, weight: (int, float), colour: str):
        if not isinstance(engine, str):
            raise TypeError("Двигатель должен быть str")
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int или float")
        if not isinstance(colour, str):
            raise TypeError("Привод должен быть str")
        self.engine = engine
        self.weight = weight
        self.colour = colour

    def __repr__(self):
        return f"{self.__class__.__name__}(engine={self.engine!r}, weight={self.weight!r}, colour={self.colour!r})"

    def __str__(self):
        return f"Двигатель {self.engine}. Вес {self.weight}. Цвет {self.colour}"

    def changecolour(self):
        colorlist = ['black', 'white', 'blue', 'green', 'yellow', 'red']  # список цветов
        newcolour = random.choice(colorlist)
        self.colour = newcolour

class drive(car):
    def __init__(self, engine: str, weight: (int, float), colour: str, wheel_drive: str):
        self.engine = None
        self.weight = None
        self.colour = None
        self.wheel_drive = None
        """Дочерний класс "Приводная(машина)".
        :param engine: Тип двигателя авто
        :param weight: Снаряженная масса авто
        :param colour: Цвет авто
        :param wheel_drive: Привод авто
        """

    def selectyarn(self):
        self.wheel_drive = random.choice(['AWD', 'RWD', 'FWD']) #привод авто

    def __str__(self):
        return f"Двигатель {self.engine}. Вес {self.weight}. Цвет {self.colour}. Привод {self.wheel_drive}"


first = car("electro", 1, "white")
first.set_params("electro", 1, "white")
first.changecolour()
print(first)

second = drive("diesel", 3, "black", "AWD")
second.set_params("diesel", 3, "black")
second.selectyarn()
print(second)
