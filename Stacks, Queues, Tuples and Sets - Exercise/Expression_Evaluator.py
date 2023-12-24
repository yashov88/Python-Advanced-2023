from collections import deque
from math import floor
from functools import reduce

expression = input().split()

idx = 0
#
# while idx < len(expression):
#     element = expression[idx]
#
#     if element == "*":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
#     elif element == "/":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
#     elif element == "+":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) + int(expression.popleft()))
#     elif element == "-":
#         for _ in range(idx - 1):
#             expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
#
#     if element in "*/+-":
#         del expression[1]
#         idx = 1
#
#     idx += 1
#
# print(floor(int(expression[0])))

functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i]))
}

while idx < len(expression):
    element = expression[idx]

    if element in "*/+-":
        expression[0] = functions[element](idx)
        [expression.pop(1) for i in range(idx)]
        idx = 1

    idx += 1

print(floor(int(expression[0])))
