# Дано N предметов массой m1, …, mN и стоимостью c1, …, cN соответственно.
# Ими наполняют рюкзак, который выдерживает вес не более M. Какую наибольшую стоимость могут иметь предметы в рюкзаке?
# Входные данные:
# В первой строке вводится натуральное число N, не превышающее 100, и натуральное число M, не превышающее 10000.
# Во второй строке вводится N натуральных чисел mi, не превышающих 100.
# Во третьей строке вводится N натуральных чисел сi, не превышающих 100.
# Выходные данные:
# Выведите одно целое число: наибольшую возможную стоимость рюкзака.


def fill_back(n, m, ms, costs):
    p, r = 0, []
    for m1, c1 in zip(ms, costs):
        r.append([c1/m1, m1, c1])
    for _, m1, c1 in sorted(r, reverse=True):
        while m - m1 >= 0:
            p += m1 * c1
            m -= m1
    return p


def assert_input(n, m, ms, costs):
    assert n <= 100, "Большое количество элементов"
    assert all([i <= 100 for i in ms]), "Элементы слишком большие"
    assert n == len(ms), "Несовпадение количества предметов и введенного числа"
    assert all([i <= 100 for i in costs]), "Элементы слишком большие"
    assert n == len(costs), "Несовпадение количество стоимости предметов и введенного числа"
    assert m <= 10**5, "Вес слишком большой"


def set_from_file(path):
    with open(path) as f:
        data = f.readlines()
    n, m = list(map(int, data[0].split()))
    ms = map(int, data[1].split())
    costs = map(int, data[2].split())
    assert_input(n, m, ms, costs)
    return fill_back(n, m, ms, costs)


def set_from_line():
    n, m = map(int, input('Введите количество предметов и вместимость рюкзака: ').split())
    ms = list(map(int, input('Введите массу каждого предмета: ').split()))
    costs = list(map(int, input('Введите стоимость каждого предмета: ').split()))
    assert_input(n, m, ms, costs)
    return fill_back(n, m, ms, costs)
