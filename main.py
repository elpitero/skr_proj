import interpreter

if __name__ == '__main__':
    tmp = ''
    expr = interpreter.Interpreter()
    while tmp.lower() != 'exit':
        tmp = input()
        if tmp.lower() != 'exit':
            expr.eval(tmp)
