import math


def get_primes(list_of_ints: list[int]):

    for el in list_of_ints:
        if el <= 1:
            continue

        for num in range(2, int(math.sqrt(el)) + 1):
            if el % num == 0:
                break
        else:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

