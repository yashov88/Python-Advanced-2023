size = int(input())

matrix = [list(input()) for _ in range(size)]

pos = [-2, -1, 1, 2]
positions = [(x, y) for x in pos for y in pos if abs(x) != abs(y)]

# positions = (
#     (-2, -1),  # up 2 left 1
#     (-2, 1),  # up 2 right 1
#     (-1, -2),  # up 1 left 2
#     (-1, 2),  # up 1 right 2
#     (2, 1),  # down 2 right 1
#     (2, -1),  # down 2 left 1
#     (1, 2),  # down 1 right 2
#     (1, -2),  # down 1 left 2
# )

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attack_position = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for position in positions:
                    position_row = row + position[0]
                    position_col = col + position[1]

                    if 0 <= position_row < size and 0 <= position_col < size:
                        if matrix[position_row][position_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attack_position = [row, col]
                    max_attacks = attacks

    if knight_with_most_attack_position:
        matrix[knight_with_most_attack_position[0]][knight_with_most_attack_position[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
