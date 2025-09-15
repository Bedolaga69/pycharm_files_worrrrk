class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("звук животного")

    def move(self):
        print(f"{self.name} двигается")

    def info(self):
        print(self.name)


# --- ПТИЦЫ ---
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)


class Vorobei(Bird):
    def make_sound(self):
        print("чирик")

    def move(self):
        print("летает по небу")


class Sinitsa(Bird):
    def make_sound(self):
        print("издает монгольское горловое пение")

    def move(self):
        print("nigga MOVE!")


# --- ДОМАШНИЕ ЖИВОТНЫЕ ---
class HomeAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(HomeAnimal):
    def make_sound(self):
        print("мяу")

    def move(self):
        print("бегает и играет")


class Dog(HomeAnimal):
    def make_sound(self):
        print("гав")

    def move(self):
        print("бегает и виляет хвостом")


# --- ЖИВОТНЫЕ В ЗООПАРКЕ ---
class ZooAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)


class Croco(ZooAnimal):
    def make_sound(self):
        print("рыг")

    def move(self):
        print("плавает в озере")


class Giraffe(ZooAnimal):
    def make_sound(self):
        print("какой-то звук")

    def move(self):
        print("шагает на длинных ногах")


# --- ПРОВЕРКА ---
animals = [
    Vorobei("Воробей"),
    Sinitsa("Синица"),
    Cat("Барсик"),
    Dog("Шарик"),
    Croco("Крокодил"),
    Giraffe("Жираф"),
]

for a in animals:
    print("----")
    a.info()
    a.make_sound()
    a.move()