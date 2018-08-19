# -*- coding: utf8 -*-


operators = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x / y),
    '^': (3, lambda x, y: x ** y)
}


def calculator(formula):
    def parser(formula_string):
        number = ''
        flag = False
        for s in range(len(formula_string)):
            if formula_string[s] in '-+':
                if s == 0:
                    flag = True
                if formula_string[s - 1] in operators:
                    flag = True
                if formula_string[s - 1] in '(':
                    flag = True
            if formula_string[s] in '1234567890.':
                number += formula_string[s]
            elif number:
                if flag:
                    yield -1 * float(number)
                else:
                    yield float(number)
                number = ''
                flag = False
            if not flag:
                if formula_string[s] in operators or formula_string[s] in '()':
                    yield formula_string[s]
        if number:
            if flag:
                yield -1 * float(number)
            else:
                yield float(number)

    def shunting_yard(formula_parsed):
        stack = list()
        for token in formula_parsed:
            if token in operators:
                while stack and stack[-1] != '(' and operators[token][0] <= operators[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ')':
                while stack:
                    x = stack.pop()
                    if x == '(':
                        break
                    yield x
            elif token == '(':
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in operators:
                y, x = stack.pop(), stack.pop()
                stack.append(operators[token][1](x, y))
            else:
                stack.append(token)
        return stack.pop()

    return calc(shunting_yard(parser(formula)))


print(calculator("-15/(7-(1+1))*3-(2+(1+1))*15/(7-(1+1))*3-(2+(1+1))*(15/(7-(1+1))*3-(2+(1+1))+15/(7-(1+1))*3-(2+(1+1)))"))
