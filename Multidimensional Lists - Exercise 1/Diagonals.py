n = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(n)]
primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n)]

print(f"Primary diagonal: {', '.join(str(el) for el in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary)}. Sum: {sum(secondary)}")
