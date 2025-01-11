class Animal:
    def _init_(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        return "Unknown sound"

    def _str_(self):
        return f"{self.name} the {self.species}"

    def _repr_(self):
        return f"{self._class_._name_}(name={self.name!r}, species={self.species!r})"

class Bird(Animal):
    def _init_(self, name, species, wingspan):
        super()._init_(name, species)
        self.wingspan = wingspan

    def fly(self):
        return f"{self.name} is flying!"

    def sound(self):
        return "Chirp chirp"

    def _str_(self):
        return f"{self.name} the {self.species} with a wingspan of {self.wingspan} cm"

# Создание объектов
animal = Animal("Lion", "Feline")
bird = Bird("Eagle", "Bird of prey", 220)

# Вывод информации о животных
print(animal)
print(bird)
print(bird.fly())
print(bird.sound())
