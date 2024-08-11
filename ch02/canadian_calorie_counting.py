# ccc06j1 - Canadian Calorie Counting
# https://dmoj.ca/problem/ccc06j1
burgerChoice = input()
if not (burgerChoice in "1234"):
    exit(f"input({burgerChoice}) is not in range: 1234")
burgerChoice = int(burgerChoice) - 1
sideChoice = input()
if not (sideChoice in "1234"):
    exit(f"input({sideChoice}) is not in range: 1234")
sideChoice = int(sideChoice) - 1
drinkChoice = input()
if not (drinkChoice in "1234"):
    exit(f"input({drinkChoice}) is not in range: 1234")
drinkChoice = int(drinkChoice) - 1
dessertChoice = input()
if not (dessertChoice in "1234"):
    exit(f"input({dessertChoice}) is not in range: 1234")
dessertChoice = int(dessertChoice) - 1
burgerCalories = [461, 431, 420, 0]
drinkCalories = [130, 160, 118, 0]
sideCalories = [100, 57, 70, 0]
dessertCalories = [167, 266, 75, 0]

totalCalories = dessertCalories[dessertChoice] + burgerCalories[burgerChoice] + sideCalories[sideChoice] + drinkCalories[drinkChoice]
print(f"Your total Calorie count is {totalCalories}.")
