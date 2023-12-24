nums = tuple(map(float, input().split()))

occ = {}

for el in nums:
    if el not in occ:
        occ[el] = 0
    occ[el] += 1

for num, count_ in occ.items():
    print(f"{num} - {count_} times")
