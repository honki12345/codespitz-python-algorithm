# ecoo17r3p1 - Baker Brie
# https://dmoj.ca/problem/ecoo17r3p1
for _ in range(10):
    franchisesAndDaysCount = input().strip().split(" ")
    if not len(franchisesAndDaysCount) == 2:
        exit(f"not {len(franchisesAndDaysCount)} == 2")
    for i in range(len(franchisesAndDaysCount)):
        if not franchisesAndDaysCount[i].isdigit():
            exit(f"not {franchisesAndDaysCount[i]} is digit")
    franchisesCount = int(franchisesAndDaysCount[0])
    dayCount = int(franchisesAndDaysCount[1])
    if not 4 <= franchisesCount <= 130:
        exit(f"not 4 <= {franchisesCount} <= 130")
    if not 2 <= dayCount <= 4745:
        exit(f"not 2 <= {dayCount} <= 4745")
    datas = []
    for i in range(dayCount):
        dayDateset = input().strip().split(" ")
        if not len(dayDateset) == franchisesCount:
            exit(f"not {len(dayDateset)} == {franchisesCount}")
        for j in range(franchisesCount):
            if not dayDateset[j].isdigit():
                exit(f"not {dayDateset[j]} is digit")
            value = int(dayDateset[j])
            if not 1 <= value <= 13_000:
                exit(f"not 1 <= {value} <= 13_000")
            dayDateset[j] = value
        datas.append(dayDateset)
    bonus = 0
    daySum = []
    for i in range(dayCount):
        dayTotal = 0
        for j in range(franchisesCount):
            dayTotal += datas[i][j]
        daySum.append(dayTotal)
        if dayTotal <= 0:
            exit(f"{dayTotal} <= 0")
        if dayTotal % 13 == 0:
            bonus += dayTotal // 13
    franchisesSum = []
    for i in range(franchisesCount):
        franchisesTotal = 0
        for j in range(dayCount):
            franchisesTotal += datas[j][i]
        franchisesSum.append(franchisesTotal)
        if franchisesTotal <= 0:
            exit(f"{franchisesTotal} <= 0")
        if franchisesTotal % 13 == 0:
            bonus += franchisesTotal // 13
    print(bonus)





