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


for perm in perms:
    print()


def remove_more_than_two_in_a_row_t(items: list[str]):
    left = []
    for item in items:
        ones = 0
        zeros = 0

        failed = False

        for x in item:

            if x == '0':
                zeros += 1
                ones = 0
            elif x == '1':
                ones += 1
                zeros = 0

            if ones == 3:
                ones = 0
                failed = True

            if zeros == 3:
                zeros = 0
                failed = True

        if not failed:
            left.append(item)

    return left


def remove_more_than_two_in_a_row_t_new(items: list[str]):
    left = []
    for item in items:
        if "111" not in item and "000" not in item:
            left.append(item)

    return left


left = remove_more_than_two_in_a_row_t_new(perms)
right = remove_more_than_two_in_a_row_t(perms)
assert left == right

perms = remove_less_than_two_in_a_row_t3(left)
perms = remove_more_than_two_in_a_row_t3(perms)
pprint(perms)

for perm in perms:
    for a in range(0, 10, 3):
        print(perm[a], end="")
    print()
