import sys

# Читаем аргументы командной строки и преобразуем их в список целых чисел
try:
    array = [int(arg) for arg in sys.argv[1:]]
except ValueError:
    print("Ошибка: Все элементы массива должны быть целыми числами.")
    sys.exit(1)
except IndexError:
    print("Ошибка: Необходимо указать хотя бы один элемент массива.")
    sys.exit(1)

# Проверяем, что массив не пустой
if not array:
    print("Ошибка: Массив не может быть пустым.")
    sys.exit(1)

# Вычисляем сумму элементов списка
sum_array = sum(array)
print("Сумма элементов списка:", sum_array)

# Вычисляем произведение элементов списка
product_array = 1
for num in array:
    product_array *= num
print("Произведение элементов списка:", product_array)

# Вычисляем среднее арифметическое всех элементов массива
average = sum_array / len(array)

# Заменяем все нулевые элементы на среднее арифметическое
for i in range(len(array)):
    if array[i] == 0:
        array[i] = average

# Выводим результат
print("Массив с замененными нулевыми элементами на среднее арифметическое:", array)