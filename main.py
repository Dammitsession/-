# 1 Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
# последних сроках и столбцах матрицы Matr2 произвольного размера.
import numpy
from numpy import *
matr2 = array([[18, 20, 22, 17], [11, 18, 21, 18], [18, 17, 23, 22], [12, 22, 20, 18]])
print('Исходная матрица:')
for i in matr2:
    print(*i)
matr2 = delete(matr2, [0], 0)
matr2 = delete(matr2, [-1], 0)
matr2 = delete(matr2, s_[0], 1)
matr2 = delete(matr2, s_[-1], 1)
matr1 = matr2
print('Полученная матрица:')
for i in matr1:
    print(*i)

# 2 Возвести в квадрат отрицательные числа
from random import randint

width, heigth = int(input('Введите ширину матрицы: ')), int(input('Введите длину матрицы: '))

matrix = [[randint(-3, 3) for j in range(width)] for i in range(heigth)]
print('До:', matrix)

math_pow = lambda value: value < 0 and pow(value, 2)

for k, v in enumerate(matrix):
    for k1, v1 in enumerate(v):
        res = math_pow(v1)
        if res:
            matrix[k][k1] = res

print('После', matrix)

#3 В матрице найти минимальный и максимальный элементы.

from random import randint

strok = int(input('Введите количество строк в матрице: '))
stolb = int(input('Введите количество столбцов в матрице: '))
mat = [[randint(0, 10) for i in range(stolb)] for j in range(strok)]
print(f"Матрица: ")

for i in mat:
    print(str(i))

up = [max(i) for i in mat]
down = [min(i) for i in mat]
print(f"Максимальный элемент матрицы: {max(up)}\nМинимальный элемент матрицы: {min(down)}")

# 4 Найти сумму отрицательных элементов первой трети матрицы.
from random import randint
strok = int(input('Введите количество строк в матрице: '))
stolb = int(input('Введите количество столбцов в матрице: '))
mat = [[randint(-10, 10) for i in range(stolb)] for j in range(strok)]
print(f"Матрица: ")
for i in mat:
    print(str(i))
s = 0
for i in range(0, round(strok/3)):
    for k in range(stolb):
        if mat[i][k] < 0:
            s += int(mat[i][k])
print('\nСумма отрицательных элементов 1й трети матрицы: =', s)

# 5 В квадратной матрице элементы на главной диагонали увеличить в 2 раза
from random import randint
import numpy as np

m, n, y, z = [int(input(i)) for i in ('Количество строк = ', 'Количество столбцов = ', 'От = ', 'До = ')]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матица: ')
for i in matrix:
    print(*i)
h = np.diagonal(matrix)
for x in range(0, len(matrix)):
    matrix[x][x] = h[x] * 2
print("Полученная матрица: ")
for i in matrix:
    print(*i)

# 6 Из матрицы сформировать массив из положительных четных элементов, найти их сумму и среднее арифметическое.
from random import randint
m, n, y, z, = [int(input(i)) for i in ('Количество строк = ', 'Количество столбцов = ', 'От = ', 'До = ')]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матица: ')
for i in matrix:
    print(*i)
h = []
for i in matrix:
   for o in i:
       if o > 0 and o % 2 == 0:
           h.append(o)
print(h, '\n' + str(sum(h)), '\n' + str(sum(h) / len(h)))

# 7 В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
import random
x = int(input('Введите размер квадратной матрицы:'))
matrix = [[random.randint(-10, 10) for i in range(x)] for j in range(x)]
print('Исходная матрица:')
for i in matrix:
    print(i)
matrix = [[matrix[i][j] * 2 if i != j else matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
print('Полученная матрица:')
for i in matrix:
    print(i)

# 8 Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
import random
x, y = [int(input(i)) for i in ('Кол-во строк:', 'Кол-во столбцов:')]
matrix = [[random.randint(-10, 10) for i in range(x)] for j in range(y)]
print('Исходная матрица:')
for i in matrix:
    print(i)
for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        if matrix[i][j] > 0:
            print(True)
            break
    break

# 9 В матрице элементы второго столбца возвести в квадрат.
from random import randint

width, heigth = int(input('Введите ширину матрицы: ')), int(input('Введите длину матрицы: '))

matrix = [[randint(1, 6) for j in range(width)] for i in range(heigth)]
print('До:', matrix)

math_pow = lambda key, value: key == 1 and pow(value, 2)

for k, v in enumerate(matrix):
    for k1, v1 in enumerate(v):
        res = math_pow(k1, v1)
        if res:
            matrix[k][k1] = res

print('После:',matrix)

# 10 Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
from random import randint

width, heigth = int(input('Введите ширину матрицы: ')), int(input('Введите длину матрицы: '))

matrix = [[randint(-3, 3) for j in range(width)] for i in range(heigth)]

print('До:', matrix)

res = lambda value: value % 2 != 0

for k, v in enumerate(matrix):
    for k1, v1 in enumerate(v):
        if res(v1):
            matrix[k][k1] = 0

print('После:',matrix)

# 11 В матрице элементы первого столбца возвести в куб.
import random
# генерация матрицы
matrix = [[0]*3 for i in range(3)]
# заполнение матрицы
for i in range(3):
    for j in range(3):
        matrix[i][j] = random.randint(-10, 10)
print("Исходная матрица:", matrix)
# изменение элементов первого столбца
for i in matrix:
    i[0] **= 3
print("Новая матрица:", matrix)

# 12 Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
import random
# генерация матрицы
matrix = [[0]*3 for i in range(3)]
# заполнение матрицы
for i in range(3):
    for j in range(3):
        matrix[i][j] = random.randint(0, 50)
print("Исходная матрица:", matrix)
# замена элементов матрицы
for i in range(3):
    for j in range(3):
        if matrix[i][j] > 10:
            matrix[i][j] = 0
print("Новая матрица:", matrix)

# 13 В матрице элементы строки N (N задать с клавиатуры) увеличить на 3
from random import randint
#  Заносим в переменные параметры матрицы
m, n, y, z, g = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ",
                                         "От = ", "До = ", "Строка, значение которой увеличим на 3 = ")]
#  заполняем матрицу случайными числами
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:', '\n', [i for i in matrix])
u = []
#  Проходимся по выбранной строке и увеличиваем элементы на 3, занося в массив u
for i in matrix[g - 1]:
    u.append(i + 3)
#  приравниваем выбранную строку матрицы к массиву
matrix[g - 1] = u
print('Полученная матрица:', '\n', [i for i in matrix])


#14  В матрице элементы последнего столбца заменить на -1
from random import randint

#  Заносим в переменные параметры матрицы
m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
#  заполняем матрицу случайными числами
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:', '\n', [i for i in matrix])
#  цикл заменения последних элементов в строке на -1
for i in range(m):
    matrix[i][n - 1] = -1
print('Полученная матрица:', '\n', [i for i in matrix])

# 15 В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.

from random import randint
m, n, y, z, r = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ", 'Столбец = ')]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print("Исходная матрциа:")
for i in matrix:
    print(*i)
for i in range(m):
    matrix[i][r-1] = matrix[i][r-1] ** 2
print('Полученная матрица:')
for i in matrix:
    print(*i)

# 16 В матрице элементы последней строки заменить на 0.

from random import randint
m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print("Исходная матрциа:")
for i in matrix:
    print(*i)
for i in range(n):
    matrix[-1][i] = 0
print('Полученная матрица:')
for i in matrix:
    print(*i)

# 17
"""В матрице элементы второго столбца заменить элементами из одномерного динамического массива соответствующей
размерности."""
from random import randint


m = int(input("Введите число строк матрицы "))
n = int(input("Введите число столбцов матрицы "))


matrix = [[randint(0, 10) for j in range(n)] for i in range(m)]
list = [randint(-10, 0) for x in range(m)]
print('Список для обновления матрицы', list)
print('Исходная матрица')
for i in matrix:
    print(*i)

for i in range(m):
    matrix[i][1] = list[i]

print('Обновленная матрица')
for i in matrix:
    print(*i)


#18
"""В матрице найти среднее арифметичское положительных элементов, кратных трем"""
from random import randint


n = int(input("Введите число строк матрицы "))
m = int(input("Введите число столбцов матрицы "))

matrix = [[randint(-10, 10) for j in range(n)] for i in range(m)]
print('Исходная матрица')
for i in matrix:
    print(*i)

three = []
for i in matrix:
    for element in i:
        if element > 0 and element % 3 == 0:
            three.append(element)

if len(three) == 0:
    print('Элементов кратных трем не встретилось')
else:
    print('Среднее арифметическое положительных элементов:', sum(three) / len(three))

#19  В матрице элементы третьей строки заменить элементами из одномерного
#  динамического массива соответствующей размерности.
from random import randint
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
matrix = [[randint(-10, 10) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(*i)
matrix[2] = [randint(-100, 100) for o in range(n)]
print('Полученная матрица:')
for i in matrix:
    print(*i)


#20  В матрице найти среднее арифметическое положительных элементов.
from random import randint
m = int(input("Введите количество строк: "))
n = int(input("Введите количество столбцов: "))
matrix = [[randint(-10, 10) for _ in range(n)] for j in range(m)]
h = []
print('Матрица:')
for i in matrix:
    print(*i)
for i in matrix:
    for o in i:
        if o > 0:
            h.append(o)
print('Среднее арифметическое положительных элементов:', sum(h) / len(h))

# 21 В матрице найти сумму и произведение элементов строки N
# (N задать с клавиатуры).
from random import randint
a = int(input('Введите количество строк матрицы: '))
b = int(input('Введите количество столбцов матрицы: '))
# создание матрицы
C = [0] * a
print('\nВаша матрица:')
for i in range(a):
    C[i] = [0] * b
for i in range(a):
    for k in range(b):
        C[i][k] = randint(-10, 10)
        if k == b-1:
            print(C[i])
n = int(input('Введите номер строки: '))
print('\n')
while n <= 0 or n > a:
    print('Такой строки нет в матрице!')
    n = int(input('\nВведите номер строки: '))
# подсчет суммы и произведения элементов выбранной строки
i = n - 1
d = 0
e = 1
for k in range(b):
    d += C[i][k]
    e *= C[i][k]
print('\nСумма элементов строки', n, '=', d)
print('Произведение элементов строки', n, '=', e)

#22 В матрице найти сумму элементов второй половины матрицы
from random import randint
a = int(input('Введите количество строк матрицы: '))
b = int(input('Введите количество столбцов матрицы: '))
# создание матрицы
C = [0] * a
print('\nВаша матрица:')
for i in range(a):
    C[i] = [0] * b
for i in range(a):
    for k in range(b):
        C[i][k] = randint(-10, 10)
        if k == b-1:
            print(C[i])
# подсчет суммы элементов второй половины матрицы
d = 0
print('\nВторая половина матрицы:')
for i in range(round(a/2), a):
    for k in range(b):
        d += int(C[i][k])
        if k == b-1:
            print(C[i])
print('\nСумма элементов второй половины матрицы =', d)

# 23 В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры).
from random import randint
J = int(input("Введите сколько будет столбцов у матрицы: "))
I = int(input("Введите сколько будет строчек у матрицы: "))
matrix = [[randint(-2, 2) for j in range(J)] for i in range(I)]
matrix_length = len(matrix)
print("Изначальная матрица:")
for i in range(matrix_length):
    print(matrix[i])
N = int(input("Введите с каким столбцом будем работать (от 1 до {}): ".format(matrix_length)))
M = N-1
result_proiz = 1
result_sum = 0
print("Значения из {} столбца:".format(N))
for i in matrix:
    for index,value in enumerate(i):
        if index == M:
            result_proiz *= value
            result_sum += value
            print(value)
print("Сумма:", result_sum)
print("Произведение:", result_proiz)

# 24 В матрице найти отрицательные элементы, сформировать из них новый массив.
# Вывести размер полученного массива.
from random import randint
J = int(input("Введите сколько будет столбцов у матрицы: "))
I = int(input("Введите сколько будет строчек у матрицы: "))
matrix = [[randint(-2, 2) for j in range(J)] for i in range(I)]
matrix_length = len(matrix)
print("Изначальная матрица:")
for i in range(matrix_length):
    print(matrix[i])
massiv_new = []
print("Отрицательные числа из матрицы:")
for i in matrix:
    for index,value in enumerate(i):
        if value < 0:
            print(value)
            massiv_new.append(value)
print("Новый массив: ", massiv_new)
print("Размер нового массива: ", len(massiv_new))

# 25  Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее
# элементов.
import numpy as np
row = int(input('Введите количество строк: '))
col = int(input('Введите количество столбцов: '))
matrix = np.random.randint(-3, 3, (row, col))
print('Исходная матрица:')
print(matrix)
print('Среднее арифметическое для каждой строки с нечетным номером:')
print(*('{} = {}'.format(i, sum(i)/len(i)) for i in matrix[::2]), sep='\n')

# 26 В матрице найти максимальный положительный элемент, кратный 4.
from random import randint
row = int(input('Введите количество строк: '))
col = int(input('Введите количество столбцов: '))
matrix = [[randint(-100, 100) for j in range(col)] for i in range(row)]
print('Исходная матрица:', matrix)
r = lambda value: value > 0 and value % 4 == 0
max_value = 0
for n, m in enumerate(matrix):
    for n1, m1 in enumerate(m):
        if r(m1):
            if m1 > max_value:
                max_value = m1
print('Максимальный положительный элемент, кратный 4:', max_value)

# 27 Для каждого столбца матрицы с четным номером найти сумму ее элементов.
from random import randint
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matrix = [[randint(-10, 10) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(*i)
matrix[1] = [sum([matrix[i][x] for i in range(n)]) for x in range(m)]
print('Полученная матрица:')
for i in matrix:
    print(*i)

#28 В матрице найти минимальный элемент в предпоследнем столбце.
import random
a = int(input('Введите количество строк: '))
b = int(input('Введите количество столбцов: '))
matr = [[random.randint(1, 10) for y in range(a)] for x in range(b)]
for i in matr:
    print(i)
n = a-2
wew = [matr[i][n] for i in range(len(matr))]
print('Минимальный элемент предпоследнего столбца: ', min(wew))

# 29 Найти суммы всех элментов одного столбца и поместить эти суммы во воторую строку матрицы
from random import randint
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matrix = [[randint(-10, 10) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(*i)
matrix[1] = [sum([matrix[i][x] for i in range(m)]) for x in range(n)]
print('Полученная матрица:')
for i in matrix:
    print(*i)

# 30 Минимальный элемент в предпоследней строке
from random import randint
j = int(input("Введите количество строк: "))
i = int(input("Введите количество столбцов: "))

matrix = [[randint(-10, 10) for y in range(j)] for x in range(i)]
for i in matrix:
    print(*i)
print('Минимальный элемент в предпоследней строке:', min(matrix[j-2]))

# 31 В матрице найти суммы элементов каждой строки и поместить их в
# новый массив. Выполнить замену элементов третьего столбца исходной
# матрицы на полученные суммы
from random import randint
m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(*i)
g = []
for p in [matrix[i] for i in range(m)]:
    g.append(sum(p))
for k in range(m):
    matrix[k][2] = g[k]
print('Полученная матрица:')
for i in matrix:
    print(*i)

# 32 В матрице найти сумму элементов второй половины матрицы
from random import randint
a = int(input('Введите количество строк матрицы: '))
b = int(input('Введите количество столбцов матрицы: '))
# создание матрицы
C = [0] * a
print('\nВаша матрица:')
for i in range(a):
    C[i] = [0] * b
for i in range(a):
    for k in range(b):
        C[i][k] = randint(-10, 10)
        if k == b-1:
            print(C[i])
# подсчет суммы элементов второй половины матрицы
d = 0
print('\nВторая половина матрицы:')
for i in range(round(a/2), a):
    for k in range(b):
        d += int(C[i][k])
        if k == b-1:
            print(C[i])
print('\nСумма элементов второй половины матрицы =', d)

# 33 Сгенерировать матрицу на произвольное количество элементов,в которой задается
# преобразование от предыдущего элемента к следующему на произвольное значение.
from random import randint
i = int(input("Введите количество строк: "))
j = int(input("Введите количество столбцов: "))
B = [[randint(-10,10) for y in range(j)] for x in range(i)]
print('Начальная матрица')
for i in B:print(*i)
for i in range(len(B)):
    for j in range(len(B[i])-1):
        B[i][j+1] += B[i][j]
print('Матрица по условию')
for i in B:print(*i)

# 34 В матрице найти сумму первых двух строк.
from random import randint
j = int(input("Введите количество строк: "))
i = int(input("Введите количество столбцов: "))
matrix = [[randint(-10,10) for y in range(j)] for x in range(i)]
print('Матрица')
for i in matrix:print(*i)
print("Сумма первых двух строк:",sum(matrix[0])+sum(matrix[1]))

#35 В матрице элементы кратные трём увеличить в 3 раза

import random
n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
matr = [[random.randint(1, 6) for j in range(n)] for i in range(m)]
print('Начальная матрица: ')
for i in matr:
    print(*i)
print('Измененная матрица: ')
izm = lambda x: x % 3 == 0
for i in matr:
    for j in i:
        if izm(j):
            j *= 3
        print(j, end=' ')
    print()

#36 В матрице найти среднее арифметическое элементов последних двух столбцов.

import numpy as np

a = np.array([[1, 2, 3], [4, 6, 8], [2, 5, 6]])
print('Начальная матрица:')

for i in a:
    print(*i)

print('Среднее арифметическое элементов последних двух столбцов: ')
print(sum(a[:, -1] + a[:, -2]) / (len(a[:, -1]) + len(a[:, -2])))



# 37 В матрице найти среднее арифметическое элементов последних двух столбцов.

import numpy as np

a = np.array([[3, 3, 3], [2, 5, 5], [6, 4, 1]])
print('Исходная матрица:')
for i in a:
    print(*i)
print('Среднее арифметическое элементов последних двух столбцов: ')
print(sum(a[:, -1] + a[:, -2]) / (len(a[:, -1]) + len(a[:, -2])))

# 38 Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
# последних сроках и столбцах матрицы Matr2 произвольного размера.

from numpy import *

matr2 = array([[18, 20, 22, 17], [11, 18, 21, 18], [18, 17, 23, 22], [12, 22, 20, 18]])
print('Исходная матрица:')
for i in matr2:
    print(*i)
matr2 = delete(matr2, [0], 0)
matr2 = delete(matr2, [-1], 0)
matr2 = delete(matr2, s_[0], 1)
matr2 = delete(matr2, s_[-1], 1)
matr1 = matr2
print('Полученная матрица:')
for i in matr1:
    print(*i)

# 41 В матрице найти минимальный элемент в предпоследней строке.
from random import randint
m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От =", "До =")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
for i in matrix:
    print(*i)
print('Минимальный элемент в предпоследней строке:', min(matrix[m-2]))

# 42 В квадратной матрице элементы на главной диагонали увеличить в 2 раза.
from random import randint
import numpy as np
m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От =", "До =")]
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:
    print(*i)
h = np.diagonal(matrix)
for x in range(0, len(matrix)):
    matrix[x][x] = h[x] * 2
print('Полученная матрица:')
for i in matrix:
    print(*i)

#43 В матрице найти минимальный элемент в предпоследнем столбце.
import random
import numpy as np
i, j = int(input('Введите количество строк: ')), int(input('Введите количество столбцов: '))
o = i * j
matrix = np.array([random.randint(-5, 5) for k in range(o)])
matrix.shape = (i, j)
print('\nИсходная матрица:\n', matrix)
tet = np.min(matrix[:, -2])
print('\nМинимальный элемент в предпоследнем столбце: {}'.format(tet))

#44 Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов
import random
import numpy as np
i, j = int(input('Введите количество строк: ')), int(input('Введите количество столбцов: '))
o = i * j
matrix = np.array([random.randint(-5, 5) for k in range(o)])
matrix.shape = (i, j)
print('\nИсходная матрица:\n', matrix)
print('\nСреднее арифметическое для каждой нечетной строки:')
print(*('({}) = {}'.format(i, sum(i)/len(i)) for i in matrix[::2]), sep='\n')

#51 В матрице найти среднее арифметическое положительных элементов.
from random import *

a = int(input("Кол-во строк матрицы: "))
b = int(input("Кол-во столбцов в матрице: "))

matr = [[randint(-10,10) for j in range(b)] for i in range(a)]
for i in matr:
    print(i)
polch = [matr[i][j] for i in range(a) for j in range(b) if matr[i][j] >= 0]
print("среднее арифметическое положительных элементов: ", round(sum(polch)/len(polch), 2))

#52 В матрице элементы первого столбца возвести в куб.
from random import *

a = int(input("Кол-во строк матрицы: "))
b = int(input("Кол-во столбцов в матрице: "))
print("Старая матрица:")
matr = [[randint(-10,10) for j in range(a)] for i in range(b)]
for d in matr:
    print(d)
print('\n', "Новая матрица:")
for i in matr:
    i[0] = i[0]**3
    print(i)

# 53 В матрице найти среднее арифметическое положительных элементов, кратных 3

from random import randint

#col, row, start, finish = [int(input(i)) for i in ("Кол-во столбцов = ", "Кол-во строк = ", "Числа от = ", "Числа до = ")]
col, row, start, finish = 5, 2, -27, 27
matrix = [[randint(start, finish) for _ in range(col)] for j in range(row)]

print('Исходная матрица: ')
for i in matrix:
    print(*i)
xd = [[i for i in j if i%3==0 and i>=0] for j in matrix]
new = []
for i in xd:
    new.extend(i)
print(f'Положительные элементы матрицы, кратные трём: {new}')
print('Их среднее арифметическое значение:', sum(new)/len(new))

# 54 В матрице элементы строки N (N задать с клавиатуры) увеличить на 3

from random import randint

col, row, start, finish, need = [int(input(i)) for i in ("Кол-во столбцов = ", "Кол-во строк = ", "Числа от = ", "Числа до = ", "Необходимая строка = ")]

matrix = [[randint(start, finish) for _ in range(col)] for j in range(row)]

print('Исходная матрица: ')
for i in matrix:
    print(*i)
g = [i + 3 for i in matrix[need-1]]
matrix[need - 1] = g
print('Результат: ')
for i in matrix:
    print(*i)

# 55 Программа меняет все элементы последней строки матрицы на 0
from random import randint as random
import re
l = [[random(0, 9) for i in range(0, 5)] for e in range(0, random(2, 4))]
print("Изначальная матрица: ", re.sub(',', '', re.sub('( \[)|(\]\])', '', re.sub('(\[\[)|(\],)', '\n', str(l)))))
l[-1] = [0 for s in l[-1]]
result = re.sub(',', '', re.sub('( \[)|(\]\])', '', re.sub('(\[\[)|(\],)', '\n', str(l))))
print("\nИтоговая матрица:    ", result)

# 56 Программа удваивает значение столбца, порядковый номер которого вводится с клавиатуры
# ПРИМЕЧАНИЕ: счёт столбцов начинается с 1
from random import randint as random
import re
a = [[random(0, 1) for i in range(0, 5)] for e in range(0, random(2, 4))]
print("Изначальная матрица: ", re.sub(',', '', re.sub('( \[)|(\]\])', '', re.sub('(\[\[)|(\],)', '\n', str(a)))))

while True:
    n = int(input('\nВведите порядковый номер столбца: ')) - 1
    if n < 0:
        print('Введите значение больше ноля')
    else: break
a = [[a[i][j] * 2 if j == n else a[i][j] for j in range(len(a[0]))] for i in range(len(a))]
print("\nИтоговая матрица:    ", re.sub(',', '', re.sub('( \[)|(\]\])', '', re.sub('(\[\[)|(\],)', '\n', str(a)))))

# 57 В матрице элементы последнего столбца заменить на -1.
import random
n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
matrix = [[random.randint(-5, 5) for i in range(n)] for j in range(m)]
print('Начальная матрица: ')
for i in matrix:
    print(*i)
for i in range(m):
    matrix[i][n - 1] = -1
print('Полученная матрица: ')
for i in matrix:
    print(*i)

# 58 В матрице элементы третьей строки заменить элементами из одномерного динамического массива соответствующей размерности.
import random
n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
matrix = [[random.randint(-5, 5) for i in range(n)] for j in range(m)]
print('Начальная матрица: ')
for i in matrix:
    print(*i)
t = n
a = [0] * t
for i in range(t):
    a[i] = int(input('Введите элементы одномерного массива: '))
print('Ваш одномерный массив: ')
for i in a:
    print(i, end='')
print('\n')
for i in range(m):
    matrix[2][i] = a[i]
print('Полученная матрица: ')
for i in matrix:
    print(*i)

#59 Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]  # вввод чисел
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
for i in range(m):  # цикл в цикле по количеству строк и столбцов
    for o in range(n):
        if matrix[i][o] > 10:  # если переменная под индексом[строка][столбец] > 10, то присвоить ей значение 0
            matrix[i][o] = 0
print('Полученная матрица:')
for i in matrix:
    print(*i)

#60 В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в 2 раза.
from random import randint

m, n, y, z = [int(input(i)) for i in ("Количество строк = ", "Количество столбцов = ", "От = ", "До = ")]  # ввод чисел
matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
print('Исходная матрица:')
for i in matrix:         # цикл по матрице и вывод без скобок каждой строки
    print(*i)
for i in range(len(matrix)):       # цикл в цикле по количеству строк и столбцов
    for j in range(len(matrix[0])):
        if i > j or i < j:
            matrix[i][j] = matrix[i][j] * 2   # цикл умножит значения на 2 по всей матрице, кроме главной диагонали
print('Полученная матрица:')
for i in matrix:
    print(*i)

# 61 сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
import random

n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
Matrix = [[random.randint(1, 5) for j in range(n)] for i in range(m)]

print('Изначальная матрица: ')
for i in Matrix:
    print(*i)


print('Измененная матрица: ')
res = lambda x: x % 2 == 1
for i in Matrix:
    for j in i:
        if res(j):
            j = 0
        print(j, end=' ')
    print()

# 62 В матрице элементы второго столбца заменить элементами из
#   одномерного динамического массива соответствующей размерности.
import random

n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
Matrix = [[random.randint(-5, 5) for i in range(n)] for j in range(m)]

print('Изначальная матрица: ')
for i in Matrix:
    print(*i)

t = n
a = [0] * t
for i in range(t):
    a[i] = int(input('Введите элементы одномерного массива: '))

print('Полученный одномерный массив: ')
for i in a:
    print(i, end='')
print('\n')

for i in range(m):
    Matrix[i][1] = a[i]

print('Измененная матрица: ')
for i in Matrix:
    print(*i)
