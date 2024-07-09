# 4. Сорт
# Дано: список из 10**6 целых чисел, каждое из которых лежит на отрезке [13, 25].
# Задача: отсортировать массив наиболее эффективным способом

# Метод сортировки подсчетом, поскольку есть большое количество повторяемых элементов.
# Сложность O(n + k) , где k - диапазон целых чисел

import random


def sort(arr):

    min_value = 13
    max_value = 25
    count = [0] * (max_value - min_value + 1)

    for number in arr:  # Считаем количество каждого числа в исходном массиве
        count[number - min_value] += 1

    sorted_arr = []
    for i in range(len(count)):  # Сортируем массив
        sorted_arr.extend([i + min_value] * count[i])

    return sorted_arr


if __name__ == '__main__':

    arr = [random.randint(13, 25) for _ in range(10 ** 6)]
    print(sort(arr)[:10])  # Первые 10 элементов отсортированного массива
