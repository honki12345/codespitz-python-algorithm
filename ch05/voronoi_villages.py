# ccc18s1 - Voronoi Villages
# https://dmoj.ca/problem/ccc18s1
villageCount = input()
if not villageCount.lstrip('-').isdigit():
    exit(f"{villageCount} != int")
villageCount = int(villageCount)
if not 3 <= villageCount <= 100:
    exit(f"input{villageCount} is not in range: 3 <= input <= 100")

positions = []
for i in range(villageCount):
    position = input().strip()
    if not position.lstrip('-').isdigit():
        exit(f"{position} != int")
    position = int(position)
    if not -1_000_000_000 <= position <= 1_000_000_000:
        exit(f"not -1_000_000_000 <= {position} <= 1_000_000_000")
    if position in positions:
        exit(f"{position} is already in positions")
    positions.append(position)

positions.sort()

minSize = 2_000_000_000
for i in range(1, villageCount - 1):
    size = positions[i + 1] - positions[i - 1]
    if size < minSize:
        minSize = size
minSize *= 0.5
print(minSize)
