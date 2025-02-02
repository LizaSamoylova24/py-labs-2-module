# TODO: Подробно описать три произвольных класса

import doctest

# TODO: описать класс

class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Инициализирует объект класса Car.

        Args:
            make (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.

        Raises:
            ValueError: Если год выпуска отрицательный или больше текущего года.

        Examples:
            >>> car = Car("Toyota", "Camry", 2020)
        """
        self.make = make
        self.model = model
        if year < 0 or year > 2023:
            raise ValueError("Год выпуска должен быть положительным и не больше текущего года.")
        self.year = year

    def get_age(self) -> int:
        """
        Возвращает возраст автомобиля.

        Returns:
            int: Возраст автомобиля в годах.

        Examples:
            >>> car = Car("Toyota", "Camry", 2020)
            >>> car.get_age()
            3
        """
        return 2023 - self.year

    def drive(self, distance: float) -> str:
        """
        Симулирует поездку на заданное расстояние.

        Args:
            distance (float): Расстояние поездки в километрах.

        Returns:
            str: Сообщение о завершении поездки.

        Raises:
            ValueError: Если расстояние отрицательное.

        Examples:
            >>> car = Car("Toyota", "Camry", 2020)
            >>> car.drive(100)
            'Поездка на 100 км завершена.'
        """
        if distance < 0:
            raise ValueError("Расстояние должно быть положительным.")
        return f"Поездка на {distance} км завершена."

    def display_info(self) -> None:
        """
        Выводит информацию о автомобиле.

        Examples:
            >>> car = Car("Toyota", "Camry", 2020)
            >>> car.display_info()
            Toyota Camry 2020
        """
        print(f"{self.make} {self.model} {self.year}")

# TODO: описать ещё класс

class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        """
        Инициализирует объект класса Book.

        Args:
            title (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц в книге.

        Raises:
            ValueError: Если количество страниц отрицательное.

        Examples:
            >>> book = Book("1984", "George Orwell", 328)
        """
        self.title = title
        self.author = author
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным.")
        self.pages = pages

    def get_summary(self) -> str:
        """
        Возвращает краткое описание книги.

        Returns:
            str: Краткое описание книги.

        Examples:
            >>> book = Book("1984", "George Orwell", 328)
            >>> book.get_summary()
            '1984 by George Orwell'
        """
        return f"{self.title} by {self.author}"

    def read(self, pages_read: int = 10) -> str:
        """
        Симулирует чтение заданного количества страниц.

        Args:
            pages_read (int): Количество страниц для чтения. По умолчанию 10.

        Returns:
            str: Сообщение о завершении чтения.

        Raises:
            ValueError: Если количество страниц для чтения отрицательное или превышает общее количество страниц.

        Examples:
            >>> book = Book("1984", "George Orwell", 328)
            >>> book.read(50)
            'Прочитано 50 страниц из 328.'
        """
        if pages_read < 0 or pages_read > self.pages:
            raise ValueError("Количество страниц для чтения должно быть положительным и не превышать общее количество страниц.")
        return f"Прочитано {pages_read} страниц из {self.pages}."

    def display_info(self) -> None:
        """
        Выводит информацию о книге.

        Examples:
            >>> book = Book("1984", "George Orwell", 328)
            >>> book.display_info()
            1984 by George Orwell, 328 pages
        """
        print(f"{self.title} by {self.author}, {self.pages} pages")



# TODO: и ещё один
class Person:
    def __init__(self, name: str, age: int, gender: str) -> None:
        """
        Инициализирует объект класса Person.

        Args:
            name (str): Имя человека.
            age (int): Возраст человека.
            gender (str): Пол человека.

        Raises:
            ValueError: Если возраст отрицательный или пол не является "male" или "female".

        Examples:
            >>> person = Person("Alice", 30, "female")
        """
        self.name = name
        if age < 0:
            raise ValueError("Возраст должен быть положительным.")
        self.age = age
        if gender not in ["male", "female"]:
            raise ValueError("Пол должен быть 'male' или 'female'.")
        self.gender = gender

    def get_age_category(self) -> str:
        """
        Возвращает категорию возраста человека.

        Returns:
            str: Категория возраста ("child", "adult", "senior").

        Examples:
            >>> person = Person("Alice", 30, "female")
            >>> person.get_age_category()
            'adult'
        """
        if self.age < 18:
            return "child"
        elif self.age < 65:
            return "adult"
        else:
            return "senior"

    def celebrate_birthday(self) -> str:
        """
        Симулирует празднование дня рождения.

        Returns:
            str: Сообщение о праздновании дня рождения.

        Examples:
            >>> person = Person("Alice", 30, "female")
            >>> person.celebrate_birthday()
            'С днём рождения, Alice! Теперь тебе 31.'
        """
        self.age += 1
        return f"С днём рождения, {self.name}! Теперь тебе {self.age}."

    def display_info(self) -> None:
        """
        Выводит информацию о человеке.

        Examples:
            >>> person = Person("Alice", 30, "female")
            >>> person.display_info()
            Alice, 30 years old, female
        """
        print(f"{self.name}, {self.age} years old, {self.gender}")