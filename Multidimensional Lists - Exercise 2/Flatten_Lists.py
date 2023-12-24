# line = input().split("|")
#
# sub_lists = []
#
# for sub_string in line[::-1]:
#     sub_lists.extend(sub_string.split())
#
# print(*sub_lists)

numbers = [sting.split() for sting in input().split("|")]

print(*[' '.join(sub_list) for sub_list in numbers[::-1] if sub_list])
