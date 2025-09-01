class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def greet(self):
        print(f"привет меня зовут {self.name}")

    def birthday(self):
        self.age += 1
        return f"с днем рождения, теперь мне {self.age} лет"

    def update_weight(self, new_weihgt):
        self.weight = new_weihgt
        return f"теперь мой вес {self.weight} кг"

    def update_height(self, new_height):
        self.height = new_height
        return f"теперь мой рост {self.height} см"

    def Human_or_woman(self):
        print(f"привет мой пол это {self.gender}")

    def info(self):
        return f"{self.name}, {self.age} лет, {self.gender}, рост {self.height} см, вес {self.weight} кг"

p = Person("анна", 30, "женский", 165, 60)
print(p.greet())
print(p.info())
print(p.birthday())
print(p.update_weight(120))
print(p.update_height(175))