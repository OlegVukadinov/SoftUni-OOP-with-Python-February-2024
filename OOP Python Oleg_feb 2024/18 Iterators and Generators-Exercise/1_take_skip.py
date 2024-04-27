class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.current_number = self.step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.iterations += 1
        if self.iterations <= self.count:
            number = self.current_number
            self.current_number += self.step
            return number - self.step
        else:
            raise StopIteration()


# Test code
# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

