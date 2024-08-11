# ecco17r1p1 - Munch 'n' Brunch
# https://dmoj.ca/problem/ecoo17r1p1
prices = [12, 10, 7, 5]
EPSILON = 1e-9
for _ in range(10):
    costOfTrip = input()
    if not costOfTrip.isdigit():
        exit(f"{costOfTrip} is not digit")
    costOfTrip = int(costOfTrip)
    if not 50 <= costOfTrip <= 50_000:
        exit(f"not 50 <= {costOfTrip} <= 50_000")
    percentages = input().strip().split(" ")
    if not len(percentages) == 4:
        exit(f"{len(percentages)} != 4")
    percentageSum = 0
    for i in range(len(percentages)):
        if not percentages[i].count(".") == 1:
            exit(f"not {percentages[i].count(".")} == 1")
        if not percentages[i].replace(".", "").isdigit():
            exit(f"not {percentages[i]} is digit")
        value = float(percentages[i])
        if not 0 <= value <= 1:
            exit(f"not 0 <= {value} <= 1")
        percentages[i] = value
        percentageSum += value
    if not 1 - EPSILON <= percentageSum < 1 + EPSILON:
        exit(f"not {percentageSum} == 1")

    studentCount = input().strip()
    if not studentCount.isdigit():
        exit(f"not {studentCount} is digit")
    studentCount = int(studentCount)
    if not 4 <= studentCount <= 2000:
        exit(f"not 4 <= {studentCount} <= 2000")

    studentSum = 0
    students = []
    for i in range(len(percentages)):
        value = int(studentCount * percentages[i])
        students.append(value)
        studentSum += value
    if studentSum < studentCount:
        students[percentages.index(max(percentages))] += studentCount - studentSum
    total = 0
    for i in range(len(percentages)):
        total += students[i] * prices[i] * 0.5
    if total < costOfTrip:
        print("YES")
    else:
        print("NO")


