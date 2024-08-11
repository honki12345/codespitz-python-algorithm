# ccc07j1 - Who is in the Middle?
# https://dmoj.ca/problem/ccc07j1
bowls = []
lightestBowl = 0
mediumBowl = 0
heaviestBowl = 0
for i in range(3):
    bowl = input()
    if not bowl.isdigit():
        exit("input is not number")
    bowl = int(bowl)
    if not 0 < bowl < 100:
        exit(f"input({bowl}) is not in range: 0 < input < 100")
    bowls.append(bowl)
bowls.sort()
print(bowls[1])
