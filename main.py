import interpreter

if __name__ == '__main__':
    tmp = ''
    expr = interpreter.Interpreter()
    while tmp != 'exit':
        tmp = input()
        expr.eval(tmp)
