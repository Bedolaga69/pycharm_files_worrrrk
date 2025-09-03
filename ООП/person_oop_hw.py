class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def __del__(self):
        print("объект удален")

    def greet(self):
        print(f"привет меня зовут {self.name}")

    def birthday(self):
        self.age += 1
        print(f"с днем рождения, теперь мне {self.age} лет")

    def update_weight(self, new_weihgt):
        self.weight = new_weihgt
        print(f"теперь мой вес {self.weight} кг")

    def update_height(self, new_height):
        self.height = new_height
        print(f"теперь мой рост {self.height} см")

    def human_or_woman(self):
        print(f"привет мой пол это {self.gender}")

    def info(self):
        print(f"{self.name}, {self.age} лет, {self.gender}, рост {self.height} см, вес {self.weight} кг")

anna = Person("анна", 30, "женский", 165, 60)
anna.greet()
anna.info()
anna.birthday()
anna.update_weight(120)
anna.update_height(175)

print("программа завершена")

def test():
    anna = Person("анна", 30, "женский", 165, 60)
test()

print("программа завершена")

anna.name = "человек пук"
anna.gender = "биба и боба"

anna.info()