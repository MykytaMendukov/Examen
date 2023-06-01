#1

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"Ім'я студента: {self.name}, Вік: {self.age}")
s = Student('Oleg', 12)
s.get_info()