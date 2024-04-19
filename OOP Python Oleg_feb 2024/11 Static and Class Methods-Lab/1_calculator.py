class Calculator:

    @staticmethod
    def add(*args):
        result = sum(args)
        return result

    @staticmethod
    def multiply(*args):
        result = args[0]  # Initialize result with the first value in args
        for value in args[1:]:
            result *= value
        return result

    @staticmethod
    def divide(*args):
        result = args[0]  # Initialize result with the first value in args
        for value in args[1:]:
            result /= value  # Divide result by each subsequent value
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]  # Initialize result with the first value in args
        for value in args[1:]:
            result -= value
        return result

# Test code
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))

