# coci12c5p1 - Ljestvica
# https://dmoj.ca/problem/coci12c5p1
composition = input()
if not 2 <= len(composition) <= 100:
    exit(f"input's len({composition}) is not in range: 2 <= input's len <= 100")
if composition[0] == '|' or composition[-1] == '|' or composition.count('||') != 0:
    exit(f"input({composition}) is invalid")
wasSeparatingMeasure = True
accentedTones = ""
for char in composition:
    if char == '|':
        wasSeparatingMeasure = True
    else:  # char != '|'
        if wasSeparatingMeasure:
            accentedTones += char
        wasSeparatingMeasure = False
aMinorTones = "ADE"
cMajorTones = "CFG"
aMinorCount = 0
cMajorCount = 0
for char in accentedTones:
    if char in aMinorTones:
        aMinorCount += 1
    else:  # not char in aMinorTones
        if char in cMajorTones:
            cMajorCount += 1
if aMinorCount > cMajorCount:
    print("A-mol")
elif aMinorCount < cMajorCount:
    print("C-dur")
else:  # aMinorCount == cMajorCount
    if composition[-1] == 'A':
        print("A-mol")
    else:  # accentedTones[-1] != 'A'
        if composition[-1] == 'C':
            print("C-dur")
