nums = [int(x) for x in input().split(' ')]
target_num = int(input())

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target_num:
#             print(f'{nums[i]} + {nums[j]} = {target_num}')


sum = set()
values = {}

for value in nums:
    if value in sum:
        sum.remove(value)
        pair = values[value]
        del values[value]
        print(f'{pair} + {value} = {target_num}')
    else:
        result = target_num - value
        sum.add(result)
        values[result] = value
