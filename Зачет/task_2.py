# 2. Задача консенсуса DNA рядов
# При чтении DNA последовательностей могут возникать единичные ошибки, выражающиеся в неверной букве в строке.
# Для решения данной проблемы требуемое место читается несколько раз, после чего строится консенсус-строка, в которой
# на каждом месте будет стоять тот символ, что чаще всего встречался в этом месте суммарно во всех чтениях.
# Т.е. для строк ATTA, ACTA, AGCA, ACAA, ACTA
#
# S = ‘ATTA ACTA …’
# data = [‘ATTA’,
#         ‘ACTA’…
# ]
# data =[
# [‘A’, ‘T’, ‘T’,’A’],
# …]
# консенсус-строка будет ACTA (в первой ячейке чаще всего встречалась A, во второй – C, в третьей – Т, в четвертой – снова А).
# Для входного списка из N строк одинаковой длины построить консенсус-строку.

from typing import Iterable


def dna(data: Iterable[str]) -> str:

    length = len(data[0])
    consensus = ""

    for i in range(length):

        count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        for string in data:
            count[string[i]] += 1
        most_common = max(count, key=count.get)  # Самый часто встречаемый
        consensus += most_common

    return consensus


if __name__ == '__main__':

    data = [
        'ATTA',
        'ACTA',
        'AGCA',
        'ACAA',
        'ACTA'
    ]
    print(dna(data))  # 'ACTA'
