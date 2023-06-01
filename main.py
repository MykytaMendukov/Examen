#8
l = []
l1 = []
for i in range(4):
    a = input('Введіть рядок: ')
    l.append(a)
def f(l):
    for n in l:
        if n.isupper():
            l1.append(n)
    return l1
print(f(l))
