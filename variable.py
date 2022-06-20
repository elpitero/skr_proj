from __future__ import annotations
from functools import total_ordering

import functions


@total_ordering
class Variable:
    def __init__(self, symbol: str, value):
        self.__symbol = symbol
        if type(value) == functions.Ans:
            self.__value = value.value
        else:
            self.__value = value

    def __iter__(self):
        return iter(self.__value)

    def __add__(self, other: Variable) -> Variable:
        return Variable(self.symbol + '_add_' + other.symbol, self.value + other.value)

    def __sub__(self, other: Variable) -> Variable:
        return Variable(self.symbol + '_sub_' + other.symbol, self.value - other.value)

    def __mul__(self, other: Variable) -> Variable:
        return Variable(self.symbol + '_mul_' + other.symbol, self.value * other.value)

    def __floordiv__(self, other: Variable) -> Variable:
        if other.value == 0:
            raise Exception("Can't divide by 0")
        return Variable(self.symbol + '/' + other.symbol, int(self.value / other.value))

    def __eq__(self, other: Variable):
        return self.__value == other.value

    def __lt__(self, other: Variable):
        return self.__value < other.value

    def __neg__(self) -> Variable:
        return Variable("-" + self.symbol, -1 * self.value)

    def __str__(self) -> str:
        return f"{self.symbol}={self.value}"

    @property
    def symbol(self):
        return self.__symbol

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class VariableContainerIterator:
    """iterator class"""

    def __init__(self, variable_container: VariableContainer):
        self.__vars = variable_container
        self.__index: int = 0

    def __next__(self):
        if self.__index < len(self.__vars):
            self.__index += 1
            return self.__vars.get_at(self.__index - 1)
        raise StopIteration


class VariableContainer:
    """container with declared variables"""

    def __init__(self):
        self.__container: list[Variable] = []
        self.__last_asked: Variable

    def __contains__(self, item: str) -> bool:
        self.__last_asked = None
        for var in self.__container:
            if item == var.symbol:
                self.__last_asked = var
                return True
        return False

    def get(self, item: str) -> Variable:
        if self.__contains__(item):
            return self.__last_asked

    def get_at(self, index: int) -> Variable:
        if 0 <= index < len(self.__container):
            return self.__container[index]
        raise IndexError("Index out of bounds")

    def insert(self, var: Variable) -> None:
        if self.__contains__(var.symbol):
            # print('hi')
            i = 0
            while i < len(self.__container):
                if self.__container[i].symbol == var.symbol:
                    del self.__container[i]
                i += 1
        self.__container.append(var)

    def __len__(self):
        return len(self.__container)

    def __str__(self):
        string = ''
        for x in self.__container:
            string = string + " " + str(x)
        return string

    def __iter__(self):
        return VariableContainerIterator(self)


if __name__ == '__main__':
    print("HI")
