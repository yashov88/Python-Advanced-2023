longest_intersection = set()

for _ in range(int(input())):
    first, second = [el.split(",") for el in input().split("-")]

    first_range = set(range(int(first[0]), int(first[1]) + 1))
    second_range = set(range(int(second[0]), int(second[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] "
      f"with length {len(longest_intersection)}")
