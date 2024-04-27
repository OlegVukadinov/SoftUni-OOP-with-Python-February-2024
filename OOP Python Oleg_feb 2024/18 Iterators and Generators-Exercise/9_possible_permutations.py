from itertools import permutations


def possible_permutations(sequence: list):
    for el in list(permutations(sequence)):
        yield list(el)


# test code
[print(n) for n in possible_permutations([1, 2, 3])]

#[print(n) for n in possible_permutations([1])]