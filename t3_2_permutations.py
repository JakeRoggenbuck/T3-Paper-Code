import itertools
from pprint import pprint

perms = [''.join(x) for x in itertools.product('01', repeat=10)]


def remove_less_than_two_in_a_row_t3(items: list[str]):
    exactly_two = []
    for x in items:
        if x[3] == '1' and x[6] == '1':
            exactly_two.append(x)

    return exactly_two


def remove_more_than_two_in_a_row_t3(items: list[str]):
    exactly_two = []
    for x in items:
        t3 = ""
        for a in range(0, 10, 3):
            t3 += x[a]

        if "111" not in t3:
            exactly_two.append(x)

    return exactly_two


def remove_more_than_two_in_a_row_t_new(items: list[str]):
    left = []
    for item in items:
        if "111" not in item and "000" not in item:
            left.append(item)

    return left


perms = remove_more_than_two_in_a_row_t_new(perms)
perms = remove_less_than_two_in_a_row_t3(perms)
perms = remove_more_than_two_in_a_row_t3(perms)
pprint(perms)

for perm in perms:
    for a in range(0, 10, 3):
        print(perm[a], end="")
    print()
