num = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(num)]

primary_sum = 0
secondary_sum = 0

for idx in range(num):
    primary_sum += matrix[idx][idx]
    secondary_sum += matrix[idx][num - idx - 1]

print(abs(primary_sum - secondary_sum))
