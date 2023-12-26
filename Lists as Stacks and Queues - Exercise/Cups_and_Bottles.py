from collections import deque

cups = deque([int(c) for c in input().split()])
bottles = deque([int(b) for b in input().split()])

wasted_liters = 0

while cups and bottles:
    current_cup = cups.popleft()
    current_bottle = bottles.pop()

    if current_cup <= current_bottle:
        wasted_liters += current_bottle - current_cup
    else:
        cups.appendleft(current_cup - current_bottle)

if cups:
    print(f"Cups: {' '.join(str(c) for c in cups)}")
else:
    print(f"Bottles: {' '.join(str(b) for b in bottles)}")

print(f"Wasted litters of water: {wasted_liters}")
