# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = {7, 8, 1, 2, 3, 4}
#
# print(a.union(b))   # {1, 2, 3, 4, 5, 6} (a | b)
# print(a.difference(b))  # {1, 2} (a - b)
# print(a.symmetric_difference(b))    # {1, 2, 5, 6} (a ^ b)
# print(a.intersection(b))    # {3, 4} (a & b)
# print(a.issubset(b))    # False (a = b)
# print(a.issubset(c))    # True (all el in A is in C) (a < c)


# p_nad_l = [
#     [300, 200, 400],
#     [200, 200, 100],
#     [450, 200, 80]
# ]
#
# print(p_nad_l[2][2])  # rows and cols


# matrix = [[1, 2, 3], [4, 5, 6]]
#
# flatten = [el for list_el in matrix for el in list_el]
#
# # for list_el in matrix:
# #     flatten.extend(list_el)
#
# print(flatten)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]    #   Matrix Representation
#
# # for i in range(len(matrix)):
# #     for j in range(len(matrix[i])):
# #         print(matrix[i][j], end=' ')
# #     print()
# [print(*inner_list) for inner_list in matrix]


# def multiply(*args):
#     res = 1
#     for num in args:
#         res *= num
#     return res
#
#
# print(multiply(1, 4, 5))
# print(multiply(4, 5, 6, 1, 3))
# print(multiply(2, 0, 1000, 5000))


# def get_info(name, age, town):
#     return f"This is {name} from {town} and he is {age} years old"
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


# my_dict = {"Petar": [2, 6], "George": [4, 4], "John": [3, 5]}
#
# print(sorted(my_dict.items(), key=lambda x: (-(sum(x[1])) / len(x[1]), x[0])))


# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
#
# print(fact(5))

# print(int("a"))

# file = open("text.txt", "r")
#
# print(type(file))
