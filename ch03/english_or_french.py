# ccc11s1 - English or French
# https://dmoj.ca/problem/ccc11s1
lines = input()
if not lines.isdigit():
    exit(f"input({lines}) is not number")
lines = int(lines)
if not 0 < lines < 10000:
    exit(f"input({lines}) is not in range: 0 < input < 10000")
sCount = 0
tCount = 0
for i in range(lines):
    sentence = input()
    if not 1 <= len(sentence) <= 100:
        exit(f"input({sentence})'s len is not in range: 1 <= input's len <= 100")
    for char in sentence:
        if char == 's' or char == 'S':
            sCount += 1
        if char == 't' or char == 'T':
            tCount += 1
if tCount > sCount:
    print("English")
elif tCount < sCount:
    print("French")
else:  # tCount == sCount
    print("French")
