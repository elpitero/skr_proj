import functions
from typing import Any, Callable
import shlex

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Ans:
    def __init__(self):
        self.__value = None

    @property
    def value(self) -> Any:
        return self.__value

    @value.setter
    def value(self, value: Any):
        self.__value = value

    def __str__(self):
        return str(self.__value)


class Interpreter:
    def __init__(self):
        self.__ans: Ans = Ans()
        self.__expr: list[str] = []
        self.__index: int = 0
        self.__keywords: dict[str, list[Any]] = {'digits': digits,
                                                 'ans': self.__ans,
                                                 'variables': functions.f_variables}
        self.__ignore: list[str] = ['=', 'is', 'than', 'do', 'else', 'to']

    def eval(self, expression: str) -> Any:
        """evaluate given expression"""
        self.__expr = shlex.split(expression)
        self.__index = -1
        self.__ans.value = self.__eval('funct')
        return self.__ans

    def __eval(self, typ: str) -> Any:
        if self.__index == len(self.__expr) - 1:
            return None
        self.__index += 1
        word = self.__expr[self.__index].lower()

        while word in self.__ignore:
            self.__index += 1
            word = self.__expr[self.__index].lower()

        return self.__check_word(word, typ)

    def __check_word(self, word: str, typ: str) -> Any:
        if typ == 'str_raw':
            return word
        if word in functions.f_variables:
            return functions.f_variables.get(word)
        if word in self.__keywords.keys():
            return self.__keywords[word]
        if word in functions.f_summary.keys():
            if typ == 'funct_raw':
                return functions.f_summary[word][0]
            return self.__call_funct(functions.f_summary[word])


# this doesn't work
        #  if typ in ['funct_raw', 'funct']:
        #    tmp = min([(x, functions.f_dist(x, word)) for x in functions.f_summary.keys()], key=lambda e: e[1])
        #    if typ == 'funct':
        #        return self.__call_funct(functions.f_summary[tmp[0]])
        #    return functions.f_summary[tmp[0]][0]
        return self.__expr[self.__index]

    def __call_funct(self, function: (Callable[[Any], Any], int)) -> Any:
        """calls function from 'functions.py'"""
        return function[0](*[self.__eval(function[2][i]) for i in range(0, function[1])])


if __name__ == '__main__':
    print("HI")
