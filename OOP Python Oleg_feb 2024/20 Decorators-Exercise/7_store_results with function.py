
def store_results(function):
    _FILE_NAME = "files/log.txt"

    def wrapper(*args, **kwargs):
        with open(_FILE_NAME, "a") as log_file:
            log_file.write(f"Function {function.__name__} was called. Result: {function(*args, **kwargs)}\n")

    return wrapper


#test code
@store_results
def add(a: int, b: int):
    return a + b

# @store_results
# def mult(a, b):
#     return a * b
#
add(6, 6)
# mult(6, 4)
