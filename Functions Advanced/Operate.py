from functools import reduce


def operate(operator, *args):
    # def sum_nums():
    #     return sum(args)
    #
    # def subtract():
    #     res = 0
    #     for num in args:
    #         res -= num
    #     return res
    #
    # def multiply():
    #     res = 1
    #     for num in args:
    #         res *= num
    #     return res
    #
    # def divide():
    #     res = 1
    #     for num in args:
    #         res /= num
    #     return res

    return reduce(lambda a, b: eval(f"{a}{operator}{b}"), args)
    # if operator == "+":
    #     return reduce(lambda a, b: a + b, args)
    # elif operator == "-":
    #     return reduce(lambda a, b: a - b, args)
    # elif operator == "*":
    #     return reduce(lambda a, b: a * b, args)
    # elif operator == "/":
    #     return reduce(lambda a, b: a / b, args)


print(operate("+", 2, 3))
print(operate("*", 3, 4))
print(operate("-", 3, 4))
print(operate("/", 3, 4))