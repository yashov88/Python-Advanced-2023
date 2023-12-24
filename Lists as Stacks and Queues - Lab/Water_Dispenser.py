# from collections import deque
#
# people = deque()
# water_quantity = int(input())
# name = input()
#
# # while name != "Start":
# #     people.append(name)
# #     name = input()
#
# command = input()

# while command != "End":
#     data = command.split()
# if len(data) == 1:
#     litters_wanted = int(data[0])
#
#     if water_quantity >= litters_wanted:
#         water_quantity -= litters_wanted
#         person = people.popleft()
#         print(f"{person} got water")
#     else:
#         person = people.popleft()
#         print(f"{person} must wait")
# else:
#     litters_refill = int(data[1])
#     water_quantity += litters_refill
# command = input()
# print(f"{water_quantity} litters_wanted left")

from collections import deque

queue = deque()
water_quantity = int(input())
name = input()

while name != 'Start':
    queue.append(name)
    name = input()

command = input()

while command != "End":
    liters = command.split()

    if "refill" in command:
        liters_refill = int(liters[1])
        water_quantity += liters_refill

    else:
        liters = int(command)
        if liters <= water_quantity:
            water_quantity-= liters
            print(f"{queue.popleft()} got water")
        else:
            print(f'{queue.popleft()} must wait')

    command = input()

print(f"{water_quantity} liters left")
