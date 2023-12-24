first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

function = {
    "Add First": lambda x: [first.add(el) for el in x],
    "Add Second": lambda x: [second.add(el) for el in x],
    "Remove First": lambda x: [first.discard(el) for el in x],
    "Remove Second": lambda x: [second.discard(el) for el in x],
    "Check Subset": lambda x: print(first.issubset(second) or second.issubset(first)),
}

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    function[command]([int(x) for x in data])

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")

#     if command == "Add First":
#         [first.add(int(el)) for el in data]
#     elif command == "Add Second":
#         [second.add(int(el)) for el in data]
#     elif command == "Remove First":
#         [first.discard(int(el)) for el in data]
#     elif command == "Remove Second":
#         [second.discard(int(el)) for el in data]
#     else:
#         print(first.issubset(second) or second.issubset(first))
