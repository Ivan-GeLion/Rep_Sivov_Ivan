# TODO Написать 3 класса с документацией и аннотацией типов
class friend:
    def __init__(self, name: str, age: int, gender: str):
        """Создание класса друг и работа с ним
        Пример:
        >>> friend1 = friend("Nick", 25, "man")
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть str")
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if not isinstance(gender, str):
            raise TypeError("Пол должен быть str")
        self.name = name
        self.age = age
        self.gender = gender

    def age_class(self, age: int):
        """Функция которая распределяет на группы по возрасту
        """
    def alphabet(self, name: str):
        """Функция которая сортирует друзей по их имени
        """

class car:
    def __init__(self, engine: str, weight: (int, float), wheel_drive: str):
        """Создание коласса машина и работа с ее характеристиками/атрибутами
        Пример:
        >>> car1 = car("electric", 2.5, "AWD")
        """
        if not isinstance(engine, str):
            raise TypeError("Двигатель должен быть str")
        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть типа int или float")
        if not isinstance(wheel_drive, str):
            raise TypeError("Привод должен быть str")
        self.engine = engine
        self.weight_class = weight
        self.wheel_drive = wheel_drive

    def weight_clases(self, weight: (int, float)) -> str:
        """Функция для определения класса автомобиля по его весу.
        Например:
        if weight <= 3.5:
            return "passenger car"
        if weight > 3.5:
            return "truck"
           Пример:
        >>> car1 = car("electric", 2.5, 'AWD')
        >>> car1.weight_clases()
        """

    def wheel_drive_class(self, wheel_drive: str) -> None:
        """Функция для определения привода автомобиля по сокрашению.
                Например:
        if wheel_drive = "FWD":
            return "Front Wheel Drive"
        if wheel_drive = "RWD":
            return "Rear Wheel Drive"
        if wheel_drive = "4WD", "AWD":
            return "All Wheel Drive"
           Пример:
        >>> car1 = car("electric", 2.5, 'AWD')
        >>> car1.wheel_drive_class()
        """

class timetable:
    def __init__(self, lesson_on_counting: int, number_classroom: int, teacher_name: str):
        """Создание и работа с учебным расписанием.
        Пример:
        >>> time1 = timetable(2, 201, 'Ivanov')
        """
        if not isinstance(lesson_on_counting, int):
            raise TypeError('Номер курса должен быть целым числом')
        if not isinstance(number_classroom, int):
            raise TypeError('Номер курса должен быть целым числом')
        if not isinstance(teacher_name, str):
            raise TypeError('Имя преподавателя должно быть str')
        self.lesson_on_counting = lesson_on_counting
        self.number_classroom = number_classroom
        self.teacher_name = teacher_name

    def double_lesson(self) -> None:
        """
            Сдвоенная пара, увеличиваем номер пары по счету на 1
            Примеры:
        >>> time1 = timetable(2, 201, 'Ivanov')
        >>> time1.double_lesson()
        """
        self.lesson_on_counting += 1

    def substituted_teacher(self, substituted_teacher_name: str) -> None:
        """Изменить преподавателя на замещающего, меняем атрибут teacher name
                Примеры:
        >>> subj1 = timetable(2, 201, 'Ivanov')
        >>> subj1.substituted_teacher('Losev')
        """
        if not isinstance(substituted_teacher_name, str):
            raise TypeError('Фамилия учителя должна быть str')
        self.teacher_name = substituted_teacher_name

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()
