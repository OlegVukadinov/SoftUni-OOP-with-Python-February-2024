
class store_results:
    _FILE_NAME = "files/log.txt"

    def __init__(self, function): # that's our decorator
        self.function = function

    def __call__(self, *args, **kwargs): #  the same as wrapper
        with open(self._FILE_NAME, "a") as log_file:
            log_file.write(f"Function {self.function.__name__} was called. Result: {self.function(*args, **kwargs)}\n")


#test code
@store_results
def add(a: int, b: int):
    return a + b

# @store_results
# def mult(a, b):
#     return a * b
#
add(2, 6)
# mult(6, 4)
