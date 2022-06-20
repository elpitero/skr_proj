from typing import TypeVar, Callable, Any, Sequence, Tuple

from sympy import ntheory
import variable
from variable import Variable, VariableContainer
import numpy as np

A = TypeVar('A')
B = TypeVar('B')


class Ans:
    def __init__(self):
        self.__value = None

    @property
    def value(self) -> Any:
        if type(self.__value) == variable.Variable:
            return self.__value.value
        return self.__value

    @value.setter
    def value(self, value: Any):
        if type(value) == Ans:
            self.__value = value.value
        else:
            self.__value = value

    def __str__(self):
        return str(self.__value)


def f_eval(eq: str) -> Any:
    """evaluates given expression"""
    d = {x.symbol: int(x.value) for x in f_variables}
    d['ans'] = f_ans.value
    try:
        return eval(eq, d)
    except NameError:
        print("Sorry, I can't evaluate this expression")
        return ""


def f_set(name, value) -> Variable:
    """sets new variable"""
    if type(name) == variable.Variable:
        name = name.symbol
    if type(value) == variable.Variable:
        value = value.value
    try:
        tmp = Variable(name, f_eval(value))
    except (TypeError, ValueError) as e:
        tmp = Variable(name, value)
    f_variables.insert(tmp)
    return tmp


def f_print(value: A) -> A:
    """prints given value"""
    if type(value) == str:
        print(f_eval(value))
    else:
        print(value)
    return value


def f_prime(value: A, other) -> bool:
    num = int(value)
    return ntheory.isprime(num)


def f_length(values: Sequence[A]) -> int:
    """calculates length of a list"""
    return len(values)


def f_contains(values: Sequence[A], item: A) -> bool:
    """checks whether item is in given set of values"""
    return item in values


def f_dist(s1: str, s2: str) -> int:
    """hi"""
    d = np.zeros((len(s1) + 1, len(s2) + 1), dtype=np.int8)  # len(s1) rows, len(s2) columns
    for i in range(1, len(s1) + 1):
        d[i, 0] = i
    for j in range(1, len(s2) + 1):
        d[0, j] = j
    for i in range(1, len(s1) + 1):  # for all rows
        for j in range(1, len(s2) + 1):  # for all columns
            if s1[i - 1] == s2[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            d[i, j] = min(d[i - 1, j] + 1,
                          d[i, j - 1] + 1,
                          d[i - 1, j - 1] + substitution_cost)
    return d[len(s1), len(s2)]


def f_lt(item: A, other: A) -> bool:
    """returns True if item < other"""
    if type(item) != variable.Variable:
        return item < type(item)(other)
    return item < other


def f_gt(item: A, other: A) -> bool:
    """returns True if item > other"""
    if type(item) != variable.Variable:
        return item > type(item)(other)
    return item > other


def f_eq(item: A, other: A) -> bool:
    """returns True if item == other"""
    if type(item) != variable.Variable:
        return item == type(item)(other)
    return item == other


def f_neq(item: A, other: A) -> bool:
    """returns True if item != other"""
    if type(item) != variable.Variable:
        return item != type(item)(other)
    return item != other


def f_geq(item: A, other: A) -> bool:
    """returns True if item >= other"""
    if type(item) != variable.Variable:
        return item >= type(item)(other)
    return item >= other


def f_leq(item: A, other: A) -> bool:
    """returns True if item <= other"""
    if type(item) != variable.Variable:
        return item <= type(item)(other)
    return item <= other


def f_range(start: A, stop: A, step: A):
    """hi"""
    return range(int(start), int(stop), int(step))


def f_mod(value: A, v2: A) -> int:
    return int(value) % int(v2)


def f_help():
    """hi"""
    for fun in f_summary.keys():
        print(fun + ' ' + f_summary[fun][0].__doc__)


f_variables = VariableContainer()
f_ans = Ans()
f_summary: dict[str, Tuple[Callable[[Any], Any], Tuple[int, int]], int] = {'help': (f_help, 0),
                                                                           'set': (f_set, 2),
                                                                           'print': (f_print, 1),
                                                                           'show': (f_print, 1),
                                                                           'length': (f_length, 1),
                                                                           'len': (f_length, 1),
                                                                           'contains': (f_contains, 2),
                                                                           'eval': (f_eval, 1),
                                                                           'equal': (f_eq, 2),
                                                                           'eq': (f_eq, 2),
                                                                           '==': (f_eq, 2),
                                                                           'greater': (f_gt, 2),
                                                                           '>': (f_gt, 2),
                                                                           'less': (f_lt, 2),
                                                                           '<': (f_lt, 2),
                                                                           '>=': (f_geq, 2),
                                                                           '<=': (f_leq, 2),
                                                                           '!=': (f_neq, 2),
                                                                           'range': (f_range, 3),
                                                                           'prime': (f_prime, 1),
                                                                           '%': (f_mod, 2)}
