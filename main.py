#5
a = input('Введіть слово: ')
def pol():
    res = a.lower()
    if res == res[::-1]:
        print(True)
    else:
        print(False)
pol()
