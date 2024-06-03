from collections.abc import Iterable

from custom_exceptions import EmptyListException


class CustomList():
    def __init__(self):
        self.__values = []

    def __check_index(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be of type integer")
        if index < 0:
            raise ValueError("Integer must be 0 or positive")
        if index >= len(self.__values):
            raise ValueError("Index is out of range")

    def append(self, value):
        self.__values.append(value)
        return self.__values

    def remove(self, index):
        self.__check_index(index)
        return self.__values.pop(index)

    def get(self, index):
        self.__check_index(index)
        return self.__values[index]

    def extend(self, iterable):
        if not isinstance(iterable, Iterable):
            raise ValueError("Value is not an iterable")

        self.__values.extend(iterable)
        return self.__values

    def insert(self, index, value):
        self.__check_index(index)
        self.__values.insert(index, value)
        return self.__values

    def pop(self):
        if not self.__values:
            raise EmptyListException("Can not pop from an empty list")

        return self.__values.pop()

    def clear(self):
        self.__values.clear()

    def index(self, value):
        if value not in self.__values:
           raise ValueError("Value is not in the list")
        return self.__values.index(value)

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return self.__values[:]

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        self.__values.insert(0, value)