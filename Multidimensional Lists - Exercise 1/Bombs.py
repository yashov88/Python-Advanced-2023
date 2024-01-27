n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]
bombs = [info.split(",") for info in input().split()]
explode_positions = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
alive_cells = 0
sum_alive_cells = 0

for bomb in bombs:
    row = int(bomb[0])
    col = int(bomb[1])
    value = matrix[row][col]
    if value > 0:
        matrix[row][col] = 0
        for idx in explode_positions:
            current_row = row + idx[0]
            current_col = col + idx[1]
            if 0 <= current_row < n and 0 <= current_col < n:
                if matrix[current_row][current_col] > 0:
                    matrix[current_row][current_col] -= value

for el_idx in matrix:
    for el in el_idx:
        if el > 0:
            alive_cells += 1
            sum_alive_cells += el

print(f'"Alive cells: {alive_cells}')
print(f'"Sum: {sum_alive_cells}')
[print(*elements) for elements in matrix]
