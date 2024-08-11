# ccc20j2 - Epidemiology
# https://dmoj.ca/problem/ccc20j2
totalPeopleHaveDisease = input()
if not totalPeopleHaveDisease.isdigit():
    exit(f"input {totalPeopleHaveDisease} is not digit")
totalPeopleHaveDisease = int(totalPeopleHaveDisease)
if not totalPeopleHaveDisease <= 10 ** 7:
    exit(f"input {totalPeopleHaveDisease} is not in range: <= 10 ^ 7")
peopleHaveDiseaseOnDay0 = input()
if not peopleHaveDiseaseOnDay0.isdigit():
    exit(f"input {peopleHaveDiseaseOnDay0} is not digit")
peopleHaveDiseaseOnDay0 = int(peopleHaveDiseaseOnDay0)
if not peopleHaveDiseaseOnDay0 <= totalPeopleHaveDisease:
    exit(f"second input {peopleHaveDiseaseOnDay0}is not less than first input {totalPeopleHaveDisease}")
numberInfectOnNextDay = input()
if not numberInfectOnNextDay.isdigit():
    exit(f"input {numberInfectOnNextDay} is not digit")
numberInfectOnNextDay = int(numberInfectOnNextDay)
if not numberInfectOnNextDay <= 10:
    exit(f"input {numberInfectOnNextDay} is not in range: <= 10")

days = 0
peopleHaveDisease = peopleHaveDiseaseOnDay0
peopleHaveInfected = peopleHaveDiseaseOnDay0
while peopleHaveDisease <= totalPeopleHaveDisease:
    peopleHaveInfected *= numberInfectOnNextDay
    peopleHaveDisease += peopleHaveInfected
    days += 1
print(days)



