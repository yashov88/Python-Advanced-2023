rows, cols = [int(el) for el in input().split(', ')]    #   Read data for rows and cols

matrix = []
sum_nums = 0

for _ in range(rows):   #   Read matrix rows
    inner_list = [int(el) for el in input().split(', ')]
    sum_nums += sum(inner_list)
    matrix.append(inner_list)

print(sum_nums)
print(matrix)
# print(matrix[0])  #   [7, 1, 3, 3, 2, 1]
# print(matrix[1])  #   [1, 3, 9, 8, 5, 6]
# print(matrix[2])  #   [4, 6, 7, 9, 1, 0]