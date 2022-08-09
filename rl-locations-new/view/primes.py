import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import math
from functools import lru_cache
from tqdm import tqdm

ones = pd.read_csv("data2/data_locations_of_ones.csv")
print("Loaded ones")
zeros = pd.read_csv("data2/data_locations_of_zeros.csv")
print("Loaded zeros")


@lru_cache(maxsize=20_000)
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def check_primes(val: int, df):
    was_prime = 0
    not_prime = 0

    odd = 0
    even = 0

    for loc, count in tqdm(zip(df['loc_in_t'], df['count'])):
        if count == val:
            if is_prime(loc):
                was_prime += 1
            else:
                not_prime += 1

            if loc % 2 == 0:
                even += 1
            else:
                odd += 1

    print(f"For {val=}: {was_prime=}, {not_prime=}, {odd=} {even=}")

check_primes(3, ones)
check_primes(6, ones)
check_primes(7, ones)
check_primes(8, ones)

check_primes(3, zeros)
check_primes(6, zeros)
check_primes(7, zeros)
check_primes(8, zeros)
