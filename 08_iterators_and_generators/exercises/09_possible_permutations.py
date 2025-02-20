from itertools import permutations


def possible_permutations(nums):

    for el in list(permutations(nums)):
        yield list(el)


[print(n) for n in possible_permutations([1, 8, 4])]
