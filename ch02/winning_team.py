# ccc19j1 - Winning Score
# https://dmoj.ca/problem/ccc19j1
aThreePointShots = input()
if not aThreePointShots.isdigit():
    exit("input is not number")
aThreePointShots = int(aThreePointShots)
if not 0 <= aThreePointShots <= 100:
    exit(f"input({aThreePointShots}) is not in range: 0 <= input <= 100")
aFieldGoals = input()
if not aFieldGoals.isdigit():
    exit("input is not number")
aFieldGoals = int(aFieldGoals)
if not 0 <= aFieldGoals <= 100:
    exit(f"input({aFieldGoals}) is not in range: 0 <= input <= 100")
aFreeThrows = input()
if not aFreeThrows.isdigit():
    exit("input is not number")
aFreeThrows = int(aFreeThrows)
if not 0 <= aFreeThrows <= 100:
    exit(f"input({aFreeThrows}) is not in range: 0 <= input <= 100")

bThreePointShots = input()
if not bThreePointShots.isdigit():
    exit("input is not number")
bThreePointShots = int(bThreePointShots)
if not 0 <= bThreePointShots <= 100:
    exit(f"input({bThreePointShots}) is not in range: 0 <= input <= 100")
bFieldGoals = input()
if not bFieldGoals.isdigit():
    exit("input is not number")
bFieldGoals = int(bFieldGoals)
if not 0 <= bFieldGoals <= 100:
    exit(f"input({bFieldGoals}) is not in range: 0 <= input <= 100")
bFreeThrows = input()
if not bFreeThrows.isdigit():
    exit("input is not number")
bFreeThrows = int(bFreeThrows)
if not 0 <= bFreeThrows <= 100:
    exit(f"input({bFreeThrows}) is not in range: 0 <= input <= 100")

aTotalScore = aFreeThrows * 1 + aFieldGoals * 2 + aThreePointShots * 3
bTotalScore = bFreeThrows * 1 + bFieldGoals * 2 + bThreePointShots * 3
if aTotalScore > bTotalScore:
    print("A")
elif aTotalScore < bTotalScore:
    print("B")
else:  # aTotalScore == bTotalScore
    print("T")
