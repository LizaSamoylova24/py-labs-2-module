from task import Car
from task import Book
from task import Person
  # Импортируем классы

if __name__ == "__main__":
    # Проверка класса Car
    try:
        car = Car("Toyota", "Camry", 2020)
        car.display_info()
        print(car.get_age())
        print(car.drive(100))
        print(car.drive(-50))  # Должно вызвать исключение
    except ValueError as e:
        print(e)

    # Проверка класса Book
    try:
        book = Book("1984", "George Orwell", 328)
        book.display_info()
        print(book.get_summary())
        print(book.read(50))
        print(book.read(-10))  # Должно вызвать исключение
    except ValueError as e:
        print(e)

    # Проверка класса Person
    try:
        person = Person("Alice", 30, "female")
        person.display_info()
        print(person.get_age_category())
        print(person.celebrate_birthday())
        print(Person("Bob", -5, "male"))  # Должно вызвать исключение
    except ValueError as e:
        print(e)
        
