first_4096 = ""

for x in range(0, 4096):
    c = "1" if bin(x).count('1') % 2 else "0"

    first_4096 += c


possible = [
    '0011001010',
    '0011001100',
    '0011011010',
    '0101001010',
    '0101001100',
    '0101011010',
    '0101101010',
    '0101101100',
]


for x in possible:
    if x in first_4096:
        print("Found")
