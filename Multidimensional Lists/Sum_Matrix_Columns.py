rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

col_sums = []
for col_idx in range(cols):
    sum_cols_el = 0
    for row_idx in range(rows):
        sum_cols_el += matrix[row_idx][col_idx]
    col_sums.append(sum_cols_el)

for col_sum in col_sums:
    print(col_sum)
