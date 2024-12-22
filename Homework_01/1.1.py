class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def makesound(self):
        print(f"{self.name} говорит: {self.sound}")

class Cat(Animal):
    def __init__(self, name: str, sound: str, color: str):
        super().__init__(name, sound)
        self.color = color

    def makesound(self):
        print(f"{self.name} (цвет: {self.color}) говорит: Мяу!")

class Dog(Animal):
    def __init__(self, name: str, sound: str, color: str):
        super().__init__(name, sound)
        self.color = color

    def makesound(self):
        print(f"{self.name} (цвет: {self.color}) говорит: Гав!")

# Примеры использования
cat = Cat(name="Кот", sound="Мяу", color="Черный")
dog = Dog(name="Собака", sound="Гав", color="Коричневый")

cat.makesound()  # Вывод: Кот (цвет: Черный) говорит: Мяу!
dog.makesound()  # Вывод: Собака (цвет: Коричневый) говорит: Гав!
