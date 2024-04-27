def read_next(*args):
    for el in args:
        #Option1
        # for sub_el in el:
        #     yield sub_el

        # Option2
        yield from el

# test code
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

# for i in read_next("Need", (2, 3), ["words", "."]):
#     print(i)
