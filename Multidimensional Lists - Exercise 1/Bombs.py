def check_indices(row1, col1, row2, col2):
    if matrix[row1][col1] > 0:
        matrix[row1][col1] -= matrix[row2][col2]
    else:
        matrix[row2][col2] -= matrix[row1][col1]


rows = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(rows)]
bombs = input().split()
# indices = all(all(el == matrix[idx] for el in matrix) for idx in range(len(bombs)))

for idx in bombs:
    row, col = [int(el) for el in idx.split(',')]

    if matrix[row][col]:

        check_indices(row - 1, col - 1, row, col)
        check_indices(row - 1, col, row, col)
        check_indices(row - 1, col + 1, row, col)
        check_indices(row, col + 1, row, col)
        check_indices(row + 1, col + 1, row, col)
        check_indices(row + 1, col, row, col)
        check_indices(row + 1, col - 1, row, col)
        check_indices(row, col - 1, row, col)

        matrix[row][col] = 0

alive_cells = 0
sum_alive_cells = 0

for el_idx in matrix:
    for el in el_idx:
        if el > 0:
            alive_cells += 1
            sum_alive_cells += el

print(f'"Alive cells: {alive_cells}')
print(f'"Sum: {sum_alive_cells}')

print(*matrix, sep='\n')
