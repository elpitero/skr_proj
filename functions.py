from typing import TypeVar, Callable, Any, Tuple, Sequence
from variable import Variable, VariableContainer
import numpy as np

A = TypeVar('A')
B = TypeVar('B')


def f_eval(eq: str) -> Any:
    """evaluates given expression"""
    try:
        return eval(eq, {x.symbol: int(x.value) for x in f_variables})
    except NameError:
        print("Sorry, I can't evaluate this expression")
        return ""


def f_set(name: str, value) -> Variable:
    """sets new variable"""
    try:
        tmp = Variable(name, f_eval(value))
    except (TypeError, ValueError) as e:
        tmp = Variable(name, value)
    f_variables.insert(tmp)
    return tmp


def f_print(value: A) -> A:
    """prints given value"""
    print(value)
    return value


def f_for(values: Sequence[A], function: Callable[[A], B]) -> list[B]:
    """calls given function for each value in values"""
    return [function(x) for x in values]


def f_length(values: Sequence[A]) -> int:
    """calculates length of a list"""
    return len(values)


def f_contains(values: Sequence[A], item: A) -> bool:
    """checks whether item is in given set of values"""
    return item in values


def f_dist(s1: str, s2: str) -> int:
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
    return item < other


def f_gt(item: A, other: A) -> bool:
    """returns True if item > other"""
    return item > other


def f_eq(item: A, other: A) -> bool:
    """returns True if item == other"""
    return item == other


def f_neq(item: A, other: A) -> bool:
    """returns True if item != other"""
    return item != other


def f_geq(item: A, other: A) -> bool:
    """returns True if item >= other"""
    return item >= other


def f_leq(item: A, other: A) -> bool:
    """returns True if item <= other"""
    return item <= other


def f_range(start: A, stop: A, step: A):
    return range(int(start), int(stop), int(step))


# def f_if(item: A, condition: Callable[[Any, Any], bool] = f_neq, other: A = None):
#    if condition(item, other)

f_variables = VariableContainer()
f_summary: dict[str, Tuple[Callable[[Any], Any], int, list[str]]] = {'set': (f_set, 2, ['str_raw', 'any']),
                                                                     'print': (f_print, 1, ['any']),
                                                                     'show': (f_print, 1, ['any']),
                                                                     'for': (f_for, 2, ['data', 'funct_raw']),
                                                                     'length': (f_length, 1, ['data']),
                                                                     'contains': (f_contains, 2, ['data', 'any']),
                                                                     'dist': (f_dist, 2, ['str', 'str']),
                                                                     'eval': (f_eval, 1, ['str']),
                                                                     'equal': (f_eq, 2, ['any', 'any']),
                                                                     'eq': (f_eq, 2, ['any', 'any']),
                                                                     '==': (f_eq, 2, ['any', 'any']),
                                                                     'greater': (f_gt, 2, ['any', 'any']),
                                                                     '>': (f_gt, 2, ['any', 'any']),
                                                                     'less': (f_lt, 2, ['any', 'any']),
                                                                     '<': (f_lt, 2, ['any', 'any']),
                                                                     '>=': (f_geq, 2, ['any', 'any']),
                                                                     '<=': (f_leq, 2, ['any', 'any']),
                                                                     'not': (f_neq, 2, ['any', 'any']),
                                                                     '!=': (f_neq, 2, ['any', 'any']),
                                                                     'range': (f_range, 3, ['int', 'int', 'int'])}
