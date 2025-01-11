class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        return "Unknown sound"

    def __str__(self):
        return f"{self.name} the {self.species}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, species={self.species!r})"

class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan

    def fly(self):
        return f"{self.name} is flying!"

    def sound(self):
        return "Chirp chirp"

    def __str__(self):
        return f"{self.name} the {self.species} with a wingspan of {self.wingspan} cm"

# Создание объектов
animal = Animal("Lion", "Feline")
bird = Bird("Eagle", "Bird of prey", 220)

# Вывод информации о животных
print(animal)
print(bird)
print(bird.fly())
print(bird.sound())
