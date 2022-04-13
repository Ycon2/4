# Преобразование вводимых значений из строковых в числовые с помощью метода integerate
def integerate(matrix):
    for i in range(len(matrix)):
        matrix[i] = int(matrix[i])
    returnmatrix


# Введение пользователем размеров матрицы
size1 = input('Введите размер матрицы №1 через пробел - ').split()
size2 = input('Введите размер матрицы №2 через пробел - ').split()
# Задание размера матриц и проверка возможности умножения
size1 = integerate(size1)
size2 = integerate(size2)


def calculate(matrix1, matrix2):
    if matrix1[1] == matrix2[0]:
        print('Матрицы возможно умножить, процесс...')
print(f'Размер матрицы №1 - {matrix1[0]}x{matrix2[1]}')
print(f'Размер матрицы №2 - {matrix1[0]}x{matrix2[1]}')
        # a и b - наше дано, c - наше искомое. Объявление их пустыми для последую-щей работы
a = []
b = []
c = []
        # Заполнение матрицы a
for i in range(matrix1[0]):
            if matrix1[1] == 1:
                a_el = int(input(f'Введите элемент строки №{i + 1} матрицы a '))
                a_el = list(a_el)
            else:
                a_el = input(
                    f'Введите строку №{i + 1} матрицы a через пробел, количество элементов - {size1[1]} ').split()
                a_el = integerate(a_el)
            a.append(a_el)
        # Заполнение матрицы b
for i in range(matrix2[0]):
            if matrix2[1] == 1:
                b_el_num = int(input(f'Введите элемент строки №{i + 1} матрицы b '))
                b_el = [b_el_num]
            else:
                b_el = input(
                    f'Введите строку №{i + 1} матрицы b через пробел, количество элементов - {matrix2[1]} ').split()
                b_el = integerate(b_el)
            b.append(b_el)
        # Начало вычислений
m = len(a)
        n = len(b)
        k = len(b[0])

        c = [[None for __ in range(k)] for __ in range(m)]  # Пустой структурированный список
        for i in range(m):  # Замена None на настоящие значения матрицы
for j in range(k):
                c[i][j] = sum(a[i][k] * b[k][j] for k in range(n))
        returnc
else:
print('Невозможно умножить матрицы, неподходящие размеры')


result = calculate(size1, size2)
print('Полученная матрица:\n', result)
