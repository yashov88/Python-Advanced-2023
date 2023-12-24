rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

max_sum = float('-inf')
sub_matrix = []

for row_idx in range(rows - 1):
    for col_idx in range(cols - 1):
        current_element = matrix[row_idx][col_idx]
        element_below = matrix[row_idx + 1][col_idx]
        next_element = matrix[row_idx][col_idx + 1]
        diagonal_element = matrix[row_idx + 1][col_idx + 1]
        sum_elements = current_element + element_below + next_element + diagonal_element

        if max_sum < sum_elements:
            max_sum = sum_elements
            sub_matrix = [[current_element, next_element], [element_below, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
