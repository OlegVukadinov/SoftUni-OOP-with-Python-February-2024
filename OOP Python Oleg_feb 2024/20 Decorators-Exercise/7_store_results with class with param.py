# with parameter
class store_results_in_file_name():
    _DIR = "files"

    def __init__(self, file_name: str):  # here goes the param
        self.file_name = file_name

    def __call__(self, function):  # this is our decorator
        def wrapper(*args, **kwargs):
            with open(f"{self._DIR}/{self.file_name}", "a") as log_file:
                log_file.write(f"Function {function.__name__} was called. Result: {function(*args, **kwargs)}\n")

        return wrapper


# test code
@store_results_in_file_name("results.txt")
def add(a: int, b: int):
    return a + b


# @store_results
# def mult(a, b):
#     return a * b
#
add(3, 6)
# mult(6, 4)
