# coci16c1p1 - Tarifa
# https://dmoj.ca/problem/coci16c1p1
mbPerMonth = input()
if not mbPerMonth.isdigit():
    exit(f"input({mbPerMonth}) is not number")
mbPerMonth = int(mbPerMonth)
if not 1 <= mbPerMonth <= 100:
    exit(f"input({mbPerMonth}) is not in range: 1 <= input <= 100")
count = input()
if not count.isdigit():
    exit(f"input({count}) is not number")
count = int(count)
if not 1 <= count <= 100:
    exit(f"input({count}) is not in range: 1 <= input <= 100")
totalMB = 0
for _ in range(count):
    totalMB += mbPerMonth
    spentMB = input()
    if not spentMB.isdigit():
        exit(f"input({spentMB}) is not number")
    spentMB = int(spentMB)
    if not 0 <= spentMB <= 10000:
        exit(f"input({spentMB}) is not in range: 0 <= input <= 10000")
    totalMB -= spentMB
totalMB += mbPerMonth
print(totalMB)