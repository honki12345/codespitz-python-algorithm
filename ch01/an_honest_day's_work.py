# (wc18c3j1) An Honest Day's Work
# https://dmoj.ca/problem/wc18c3j1
p = input()
if not p.isdigit():
    exit("input is not digit")
leftoverLitres = int(P)
if not 1 <= leftoverLitres <= 100:
    exit("leftover litres is not in range: 1 <= p <= 100")

b = input()
if not b.isdigit():
    exit("input is not digit")
costLitres = int(B)
if not 1 <= costLitres <= 100:
    exit("cost litres is not in range: 1 <= b <= 100")

d = input()
if not d.isdigit():
    exit("input is not digit")
badgePrice = int(d)
if not 1 <= badgePrice <= 100:
    exit("badge price is not in range: 1 <= b <= 100")

badgeCount = leftoverLitres // costLitres
unusedLitres = leftoverLitres % costLitres
totalBadgePrice = badgeCount * badgePrice
unusedLitresPrice = unusedLitres * 1
print(totalBadgePrice + unusedLitresPrice)
