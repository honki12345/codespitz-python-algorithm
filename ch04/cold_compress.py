# ccc19j3 - Cold Compress
# https://dmoj.ca/problem/ccc19j3
number = input()
if not number.isdigit():
    exit(f"input({number}) is not number")
number = int(number)
for i in range(number):
    line = input()
    if not 1 <= len(line) <= 80:
        exit(f"input({line}) is not in range: 1 <= line <= 80")
    encodedLine = ""
    prevChar = line[0]
    charCount = 0
    line += " "
    for char in line:
        if char == prevChar:
            charCount += 1
        else:  # char != prevChar
            encodedLine += str(charCount) + " " + prevChar + " "
            prevChar = char
            charCount = 1
    print(encodedLine[:-1])
