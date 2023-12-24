from statistics import mean
from collections import defaultdict

n = int(input())

students_grades = defaultdict(lambda: [])

for _ in range(n):
    name, grade = tuple(input().split())
    grade = float(grade)

    # if name not in students_grades:
    #     students_grades[name] = []
    students_grades[name].append(grade)

for name, grades in students_grades.items():
    avg = mean(grades)
    print(f"{name} -> {' '.join([str(f'{grade:.2f}') for grade in grades])} (avg: {avg:.2f})")
