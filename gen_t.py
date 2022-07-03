for x in range(0, 2000, 3):
    c = bin(x).count('1') % 2

    print(c, end="")
print()
