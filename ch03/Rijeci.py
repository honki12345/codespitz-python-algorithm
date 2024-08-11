# coci13c3p1 - Rijeci
# https://dmoj.ca/problem/coci13c3p1
pressTimes = input()
if not pressTimes.isdigit():
    exit(f"input({pressTimes}) is not number")
pressTimes = int(pressTimes)
if not 1 <= pressTimes <= 45:
    exit(f"input({pressTimes}) is not in range: 1 <= input <= 45")
screen = "A"
aCount = 1
bCount = 0
for i in range(pressTimes):
    aCountTmp = aCount
    bCountTmp = bCount
    bCount += aCountTmp
    aCount += bCountTmp
    aCount -= aCountTmp
print(f"{aCount} {bCount}")

