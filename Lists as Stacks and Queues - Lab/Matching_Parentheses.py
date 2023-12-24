text = input()
stack_parent = []

for i in range(len(text)):
    if text[i] == "(":
        stack_parent.append(i)
    elif text[i] == ")":
        start_position = stack_parent.pop()
        end_position = i + 1
        print(text[start_position:end_position])
