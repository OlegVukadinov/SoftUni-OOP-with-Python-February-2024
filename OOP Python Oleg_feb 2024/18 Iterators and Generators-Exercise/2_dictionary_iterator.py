class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.element = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.element += 1
        if self.element < len(self.dictionary):
            return tuple(self.dictionary.items())[self.element]
        else:
            raise StopIteration()
# Test code
# result = dictionary_iter({1: "1", 2: "2"})
# for x in result:
#     print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

