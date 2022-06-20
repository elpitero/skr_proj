import functions
from typing import Any, Callable
import shlex

import variable

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Interpreter:
    def __init__(self):
        self.__ans: functions.Ans = functions.f_ans
        self.__expr: list[str] = []
        self.__index: int = 0
        self.__ignore: list[str] = ['=', 'if', 'is', 'are']
        self.__keywords: dict[str, Any] = {'digits': digits,
                                           'ans': self.__ans,
                                           'variables': functions.f_variables}

    def eval(self, expression: str) -> Any:
        """evaluate given expression"""
        self.__expr = shlex.split(expression)

        self.__index = -1
        result = 0

        if self.__expr[0].lower() == 'exit':
            return True
        while result is not None:
            result = self.__eval()
            if result is not None:
                self.__ans.value = result
        return str(self.__ans)

    def __eval(self) -> Any:
        if self.__index == len(self.__expr) - 1:
            return None
        self.__index += 1
        word = self.__expr[self.__index].lower()

        while word in self.__ignore and self.__index < len(self.__expr) - 1:
            self.__index += 1
            word = self.__expr[self.__index].lower()

        if word in functions.f_variables:
            return functions.f_variables.get(word)
        if word in self.__keywords.keys():
            return self.__keywords[word]
        if word == 'for':
            self.__for()
        if word in functions.f_summary.keys():
            if self.__index == len(self.__expr) - 1:
                return functions.f_summary[word][0]
            return self.__call_funct(functions.f_summary[word])

        return word

    def __call_funct(self, function: (Callable[[Any], Any], int)) -> Any:
        """calls function from 'functions.py'"""
        # return function[0](*[self.__eval() for i in range(0, function[1])])
        print([self.__eval() for i in range(0, function[1])])

    def __for(self):
        end = int(self.__eval())
        c = self.__index
        result = 0
        for i in range(0, end):
            result = 0
            self.__index = c
            while result is not None:
                result = self.__eval()
        return result


if __name__ == '__main__':
    print("HI")
