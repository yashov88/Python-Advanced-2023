rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

sum_diagonal = 0

for idx in range(rows):
    sum_diagonal += matrix[idx][idx]

print(sum_diagonal)
