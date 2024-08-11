# ccc18j2 - Occupy parking
# https://dmoj.ca/problem/ccc18j2
spaces = input()
if not spaces.isdigit():
    exit(f"input({spaces}) is not number")
spaces = int(spaces)
if not 1 <= spaces <= 100:
    exit(f"input({spaces}) is not in range: 1 <= input <= 100")
yesterday = input()
if not yesterday.count('C') + yesterday.count('.') == len(yesterday):
    exit(f"input({yesterday}) not consist of C .")
today = input()
if not today.count('C') + today.count('.') == len(today):
    exit(f"input({today}) not consist of C .")

occupiedCount = 0
for i in range(spaces):
    if yesterday[i] == 'C' and yesterday[i] == today[i]:
        occupiedCount += 1
print(occupiedCount)

