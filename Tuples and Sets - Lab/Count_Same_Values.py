nums = tuple([float(num) for num in input().split()])
#nums = tuple(map(float, input().split()))

occ = {}

# for el in nums:
#     if el not in occ:
#         occ[el] = 0
#     occ[el] += 1
#
# for num, count in occ.items():
#     print(f"{num} - {count} times")


for el in nums:
    occ[el] = nums.count(el)

for num, count in occ.items():
    print(f"{num} - {count} times")