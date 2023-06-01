#3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def get_info(self):
        print(f'Назва: {self.title}, Автор: {self.author}')
b = Book('1984', 'Джордж Орвелд')
b.get_info()