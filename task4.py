# Дано N предметов массой m1, …, mN. Ими наполняют рюкзак, который выдерживает вес не более M. Как набрать вес
# в точности M, используя как можно меньше предметов?

# Входные данные:
# Первая строка входных данных содержит натуральное число N, не превышающее 100, и натуральное число M,
# не превышающее 10000.
# Во второй строке находится N натуральных чисел mi, не превышающих 100.

# Выходные данные:
# Выведите наименьшее необходимое число предметов или 0, если набрать данный вес невозможно.


def min_things(ml, m):
    ml = sorted(ml, reverse=True)
    result = 0
    for i in ml:
        s1, d = divmod(m, i)
        if not s1:
            m = d
            continue
        result += s1
        m -= i * s1
    return result if result else 0


def assert_input(n, m, x):
    assert n <= 100, "Большое количество элементов"
    assert all([i <= 100 for i in x]), "Элементы слишком большие"
    assert n == len(x), "Несовпадение количества элементов и введенного числа"
    assert m <= 10000, "Вес слишком большой"


def set_from_file(path):
    with open(path) as f:
        n, m = map(int, f.readline().split())
        x = list(map(int, f.readline().split()))
    assert_input(n, m, x)
    return min_things(x, m)


def set_from_line():
    n = int(input('Введите количество элементов: '))
    x = list(map(int, input('Введите последовательность весов предметов: ').split()))
    m = int(input("Введите максимально возможный вес: "))
    assert_input(n, m, x)
    return min_things(x, m)


if __name__ == '__main__':
    print(set_from_file('data.txt'))
    # print(set_from_line())
