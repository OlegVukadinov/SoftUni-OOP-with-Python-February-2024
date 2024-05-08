def number_increment(numbers):

    def increase():
        return [el + 1 for el in numbers]

    return increase()


#Test code
print(number_increment([1, 2, 3]))