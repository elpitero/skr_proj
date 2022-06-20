from interpreter import Interpreter

# run from terminal with python -m pytest test_pytest.py -vvv

def test1(monkeypatch):
    """print 10th fibonacci number"""
    expr = Interpreter()
    monkeypatch.setattr('builtins.input', lambda _: "set tmp 0 set prev 1 set prev2 = 1 set act = 2")
    expr.eval(input("hi"))
    monkeypatch.setattr('builtins.input', lambda _: "for 7 set act = act+prev set tmp = prev set prev prev+prev2 set "
                                                    "prev2 tmp")
    expr.eval(input("hi"))
    monkeypatch.setattr('builtins.input', lambda _: "print act")
    assert expr.eval(input("hi")) == 'act=55'


def test2(monkeypatch):
    """print prime numbers in range"""
    expr = Interpreter()
    monkeypatch.setattr('builtins.input', lambda _: "set a = range 1 9 1")
    expr.eval(input("hi"))
    monkeypatch.setattr('builtins.input', lambda _: "foreach a if is prime")
    expr.eval(input("hi"))
    monkeypatch.setattr('builtins.input', lambda _: "print ans")
    assert expr.eval(input("hi")) == '[2, 3, 5, 7]'


def test3(monkeypatch):
    """print 2 digit numbers divisible by 9"""
    expr = Interpreter()
    monkeypatch.setattr('builtins.input', lambda _: "set a = range 10 100 1")
    expr.eval(input("hi"))
    monkeypatch.setattr('builtins.input', lambda _: "foreach a == 0 % 9")
    expr.eval(input("hi"))
    monkeypatch.setattr('builtins.input', lambda _: "print ans")
    assert expr.eval(input("hi")) == '[18, 27, 36, 45, 54, 63, 72, 81, 90, 99]'
