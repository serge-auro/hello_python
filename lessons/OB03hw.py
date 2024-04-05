# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f'{self.name} makes sound')

    def eat(self):
        print(f'{self.name} is eating')

class Bird(Animal):
    def __init__(self, name, age, sound, wings_type):
        super().__init__(name, age)
        self.sound = sound
        self.wings_type = wings_type

    def make_sound(self):
        print(self.sound)

class Mammal(Animal):
    def __init__(self, name, age, sound, size):
        super().__init__(name, age)
        self.sound = sound
        self.size = size

    def make_sound(self):
        print(self.sound)

class Reptile(Animal):
    def __init__(self, name, age, sound, tile_type):
        super().__init__(name, age)
        self.sound = sound
        self.tile_type = tile_type

    def make_sound(self):
        print(self.sound)


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def make_sound(self):
        print(f'Hello, my name is {self.name}, {self.position}')

class ZooKeeper(Employee):
    def __init__(self, name, age):
        super().__init__(name, age, 'ZooKeeper')

    def feed_animal(self, animal):
        print(f'{self.name} is feeding {animal.name}')

class Veterinarian(Employee):
    def __init__(self, name, age):
        super().__init__(name, age, 'Veterinarian')

    def heal_animal(self, animal):
        print(f'{self.name} is healing {animal.name}')

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, name, age, sound, spec_type, type):
        if type == 'bird':
            new_animal = Bird(name, age, sound, spec_type)
        elif type == 'mammal':
            new_animal = Mammal(name, age, sound, spec_type)
        elif type == 'reptile':
            new_animal = Reptile(name, age, sound, spec_type)
        else:
            new_animal = Animal(name, age, sound)
        self.animals.append(new_animal)

    def add_employee(self, name, age, position):
        if position == 'zookeeper':
            new_employee = ZooKeeper(name, age)
        elif position == 'veterinarian':
            new_employee = Veterinarian(name, age)
        else:
            new_employee = Employee(name, age, position)
        self.employees.append(new_employee)

    def display_zoo_info(self):
        if len(self.animals) > 0:
            print("Animals in the zoo:")
            for animal in self.animals:
                print(f"{animal.name} {str(animal.age)}")
        else:
            print("No animals in the zoo")

        if len(self.employees) > 0:
            print("\nEmployees working in the zoo:")
            for employee in self.employees:
                print(f"{employee.name} - {employee.position}")
        else:
            print("No employees working in the zoo\n")

    def make_noise(self):
        print("\nAnimals, make a noise!")
        for animal in self.animals:
            animal.make_sound()

    def say_hi(self):
        print("\nHello Zoo!")
        for employee in self.employees:
            employee.make_sound()

    def load_zoo_info(self, file_name):
        with open(file_name, 'r') as file:
            data = eval(file.read())
            self.animals = data["animals"]
            self.employees = data["employees"]

    def save_zoo_info(self, file_name):
        data = {
            "animals": self.animals,
            "employees": self.employees
        }
        with open(file_name, 'w') as file:
            file.write(str(data))


print('start')
my_zoo = Zoo()
my_zoo.display_zoo_info()

my_zoo.add_animal('Pretty', 5, "Coo coo", 'short', "bird")
my_zoo.add_animal('Scratch', 6, "Hoo hoo", 'long', "bird")
my_zoo.add_animal('Donny', 8, "Meow", 'middle', "mammal")
my_zoo.add_animal('Meggy', 12, "Woof", 'big', "mammal")
my_zoo.add_animal('Marta', 1, "Shee", 'ling tile', "reptile")
my_zoo.add_animal('Rose', 2, "Shoo", 'no tile', "reptile")
my_zoo.add_animal('Mimi', 3, "Yik yik", 'big', "reptile")

# Добавляем сотрудников
my_zoo.add_employee("Alice", 32,"zookeeper")
my_zoo.add_employee("Bob", 45, "veterinarian")
my_zoo.add_employee("Ivan", 45, "director")

# Load information from a file
# my_zoo.load_zoo_info("zoo_info.json")

# Display zoo information
my_zoo.display_zoo_info()

# Save information to a file
my_zoo.save_zoo_info("zoo_info.json")


my_zoo.make_noise()
my_zoo.say_hi()
