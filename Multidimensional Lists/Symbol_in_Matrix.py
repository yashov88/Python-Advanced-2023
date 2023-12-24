def find_element_in_matrix(matrix, element):
    for row_idx in range(n):
        for col_idx in range(n):
            if matrix[row_idx][col_idx] == element:
                return (row_idx, col_idx)


n = int(input())

matrix = []

for _ in range(n):
    inner_list = list(input())
    matrix.append(inner_list)

searched_symbol = input()
positional = find_element_in_matrix(matrix, searched_symbol)

if positional:
    print(positional)
else:
    print(f"{searched_symbol} does not occur in the matrix")
