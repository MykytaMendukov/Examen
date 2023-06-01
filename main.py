#9
l2 = []
def f(l):
    l1 = l.split(' ')
    print(l1)
    for i in l1:
        if 'Python' in i:
            l2.append(i)
print(f'Список з слів, що мають у собі "Python": {l2}')
l = input('Введіть слова через пробіл:')
f(l)
