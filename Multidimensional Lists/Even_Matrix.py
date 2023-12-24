row = int(input())

matrix = []

for row_idx in range(row):
    inner_list = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
    matrix.append(inner_list)

print(matrix)
