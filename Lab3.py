class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self._name = name
        self._author = author
        self.pages = None
        self.set_pages(pages)

    def set_pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        self.pages = new_pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    def __str__(self):
        return f"Бумажная книга {self._name}. Автор {self._author}. Число страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self._name = name
        self._author = author
        self.duration = None
        self.set_duration(duration)

    def set_duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Длительность должна быть типа float")
        self.duration = new_duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

    def __str__(self):
        return f"Аудиокнига {self._name}. Автор {self._author}. Длительность: {self.duration}"
