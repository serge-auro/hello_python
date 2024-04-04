from random import randint


class Warrior():

    def __init__(self, name, endurance, health, strength, intelligence, dexterity, hair_color):
        self.name = name
        self.endurance = endurance
        self.health = health
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} is sleeping")
        if self.endurance < 100:
            self.endurance = round(self.endurance * 1.2)
    def eat(self):
        print(f"{self.name} is eating")
        if self.health < 100:
            self.health = round(self.health * 1.2)

    def hit(self):
        print(f"{self.name} is hitting")
        self.endurance -= 10

    def walk(self):
        print(f"{self.name} is walking")

    def info(self):
        print(f"Name: {self.name}; endurance: {self.endurance}; health: {self.health}; strength: {self.strength}; intelligence: {self.intelligence}; dexterity: {self.dexterity} hair_color: {self.hair_color}")


warrior1 = Warrior("Morgan", randint(50,100), randint(60,100), randint(10,100), randint(10,100), randint(10,100), "blue")

warrior2 = Warrior("Dolly", randint(50,100), randint(60,100), randint(10,100), randint(10,100), randint(10,100), "pink")

warrior1.info()
warrior2.info()

warrior1.sleep()
warrior1.eat()
warrior1.hit()
warrior1.walk()
warrior1.info()
