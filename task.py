class Animal:
    def init(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        return "Unknown sound"

    def str(self):
        return f"{self.name} the {self.species}"

    def repr(self):
        return f"{self.class.name}(name={self.name!r}, species={self.species!r})"

class Bird(Animal):
    def init(self, name, species, wingspan):
        super().init(name, species)
        self.wingspan = wingspan

    def fly(self):
        return f"{self.name} is flying!"

    def sound(self):
        return "Chirp chirp"

    def str(self):
        return f"{self.name} the {self.species} with a wingspan of {self.wingspan} cm"

# Создание объектов
animal = Animal("Lion", "Feline")
bird = Bird("Eagle", "Bird of prey", 220)

# Вывод информации о животных
print(animal)
print(bird)
print(bird.fly())
print(bird.sound())
