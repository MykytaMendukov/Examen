#6
import random
l = []
for i in range(6):
    i = random.randint(1, 10)
    l.append((i))
print(f'Початковий список: {l}')
l1 = []
for n in l:
    if n % 2 == 0:
        l1.append(n)
print(f'писок з парними числами: {l1}')
