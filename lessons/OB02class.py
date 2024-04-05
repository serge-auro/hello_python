class Bird:
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f'Bird {self.name} flying')

    def eat(self):
        print(f'Bird {self.name} eating')

    def sing(self):
        print(f'Bird {self.name} singing')

    def info(self):
        print(f'Bird name: {self.name}; voice: {self.voice}; color: {self.color} ')


class Pigeon(Bird):
    def __init__(self, name, voice, color, favourite_food):
        super().__init__(name, voice, color)
        self.favourite_food = favourite_food

    def walk(self):
        print(f'Bird {self.name} walking')

    def sing(self):
        super().sing()
        print(f"{self.voice} {self.voice}")


class Test:
    def __init__(self):
        self.public = "public attr"
        self._protected = "protected attr"
        self.__private = "private attr"

    def get_private(self):
        return self.__private

# MAIN
test = Test()

print(test.public)
print(test._protected)
print(test.get_private())
print(test._Test__private)

bird1 = Pigeon('Page', 'Coo coo', 'blue', 'bread crumbs')
bird2 = Bird('Spirit', 'Chirp chirp', 'brown')
print(bird1.name)
bird1.sing()
bird1.info()
bird1.walk()

# 1. Parrot - "Polly wants a cracker"
# 2. Owl - "Hoo hoo"
# 3. Pigeon - "Coo coo"
# 4. Duck - "Quack quack"
# 5. Eagle - "Screech screech"
