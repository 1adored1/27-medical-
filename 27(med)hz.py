f = open('26.txt')
n = int(f.readline())
length = []
value = []
prev = 1
k = 36
# создание 2 массивов. В массиве <a> номера пунктов (расстояние от 0). В массиве <b> необходимое кол-во контейнеров
for i in range(n):
    z, x = map(int, f.readline().split())
    if z != 1 and len(length) == 0:  # добавление нулевого элемента (под #1) (если такого нет) в оба массива
        length.insert(0, 1)
        value.insert(0, 0)
    c = x // k if x % k == 0 else x // k + 1  # вычисление необходимого кол-ва контейнеров
    if z - prev > 1:
        for x in range(prev + 1, z):  # добавление всех пропущенных пунктов по порядку (с 0 необходимых контейнеров)
            length.append(x)
            value.append(0)
    prev = z  # обновление предыдущего числа
    length.append(z)
    value.append(c)

# сумма, если лаборатория на нулевой позиции (под #1)
sums = [0] * n
for i in range(n):
    sums[0] += value[i] * (length[i] - 1)

s_l = value[0]  # сумма чисел слева от лаборатории (включая лабораторию)
s_r = sum(value[1:])  # сумма чисел справа от лаборатории
mn = float('inf')
for i in range(1, n):
    sums[i] += sums[i - 1] + s_l - s_r  # изменение суммы нынешней позиции
    s_l += value[i]  # изменение суммы чисел слева от лаборатории
    s_r -= value[i]  # изменение суммы чисел справа от лаюборатории
    if sums[i] < mn and length[i] != 0:  # вычисление минимальной суммы и самой выгодной позиции для лаборатории
        mn = sums[i]
        counter = i + 1
print(mn)
print(counter)