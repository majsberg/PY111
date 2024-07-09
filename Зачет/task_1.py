# 1. Считалочка
# Дано N человек, считалка из K слогов. Считалка начинает считать с первого человека.
# Когда считалка досчитывает до k-го слога, человек, на котором она остановилась, вылетает.
# Игра происходит до тех пор, пока не останется последний человек.
# Для данных N и К дать номер последнего оставшегося человека.
# [1,2,3,4,5,6,7] k = 3
# [1,2,4,5,6,7]
# [1,2,4,5,7]
# [1,4,5,7]
# [1,4,5]
# [1,4]
# [4]

def counting(n: list, k: int) -> int:

    index = 0  # Начало считалочки

    # Пока не останется последний человек
    while len(n) > 1:
        index = (index + k - 1) % len(n)
        n.pop(index)

    return n[0]  # Последний оставшийся человек


if __name__ == '__main__':
    n = [1, 2, 3, 4, 5, 6, 7]    # Количество человек
    k = 3                        # Слогов считалочки
    print(counting(n, k))  # 4
