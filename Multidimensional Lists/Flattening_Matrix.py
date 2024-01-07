rows = int(input())

flatten = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(', ')]
    flatten.extend(inner_list)

print(flatten)
