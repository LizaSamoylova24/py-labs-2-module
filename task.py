class Animal: #задаем основной класс
    def __init__(self, name, species): #опредеяем какие будут аргументы
        self.name = name #создаем атрибут
        self.species = species #создаем атрибут

    def sound(self): #метод sound возвращающий значение Unknown sound 
        return "Unknown sound"

    def __str__(self): #метод возвращающий строку в формате "название вид"
        return f"{self.name} the {self.species}"

    def __repr__(self): # метод создающий строку, которую можно использовать для создания экземпляра класса
        return f"{self.__class__.__name__}(name={self.name!r}, species={self.species!r})"

class Bird(Animal): #задаем подкласс (наследуемый)
    def __init__(self, name, species, wingspan): #конструктор класса с тремя аргументами
        super().__init__(name, species) #вызываем конструктор базового класса для инициализациии атрибутов name и species
        self.wingspan = wingspan #создаем атрибут wingspan 

    def fly(self): #определяем метод, для возвращения строки
        return f"{self.name} is flying!"

    def sound(self): #метод возвращающий строку 
        return "Chirp chirp"

    def _str_(self): #метод возвращающий строковое представление объекта
        return f"{self.name} the {self.species} with a wingspan of {self.wingspan} cm"

# Создание объектов
animal = Animal("Lion", "Feline") #создание объекта
bird = Bird("Eagle", "Bird of prey", 220) #тоже самое, другой метод

# Вывод информации о животных
print(animal)
print(bird)
print(bird.fly())
print(bird.sound())
