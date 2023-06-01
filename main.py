#9
l2 = []
def f(l):
    l1 = l.split(' ')
    for i in l1:
        if 'Python' in i:
            l2.append(i)
l = input('Введіть слова через пробіл:')
f(l)
print(f'Список з слів, що мають у собі "Python": {l2}')
