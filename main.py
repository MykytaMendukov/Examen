#4
# Створіть клас Animal (тварина) з атрибутами name (ім'я) і
# sound (звук). Додайте метод make_sound, який виводить
# звук, який робить тварина.

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    def make_sound(self):
        print(f'{self.name} робить "{self.sound}!"')
a1 = Animal('Собака', 'Гав')
a2 = Animal('Котик', 'Мяу')
a1.make_sound()
a2.make_sound()