#7
d = {}
l = []
for i in range(3):
    name = input("Введіть ім'я: ")
    mark = int(input('Введіть оцінку: '))
    d[name] = mark
mars_m = max(d, key=d.get)
print(mars_m)