def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper
@singleton
class Person:

    def __init__(self):
        self.name = "Test"


p = Person()
print(id(p))

p2 = Person()
print(id(p2))