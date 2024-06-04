# Дан набор гирь массой m1, …, mN. Можно ли их разложить на две чаши весов, чтобы они оказались в равновесии?
# Входные данные:
# В первой строке вводится натуральное число N, не превышающее 100.
# Во второе строке вводится N натуральных чисел mi, не превышающих 100.
# Выходные данные:
# Выведите True или False

from random import shuffle


def compare_arr(n, m):
    left = [[i] for i in m]
    right = []
    for i in range(n):
        m1 = m.copy()
        m1.remove(m[i])
        right.append(m1)
    result = []
    while len(right[0]) > 0:
        for i in range(n):
            result.append(sum(left[i]) == sum(right[i]))
        if any(result):
            return True
        for i in range(n):
            var = right[i].pop()
            left[i].append(var)
    else:
        return False


if __name__ == '__main__':
    n = int(input('Введите количество чисел: '))
    m = list(map(int, input('Введите цифры через пробел: ').split()))
    assert n <= 100, 'Неверное количество цифр'
    assert any([i <= 100 for i in m]), 'Использованы цифры больше 100'
    assert len(m) == n, 'Разная длина'
    print(compare_arr(n, m))


