# wc17c3j3 - Uncrackable
# https://dmoj.ca/problem/wc17c3j3
password = input()
flag = True
if not 1 <= len(password) <= 100:
    exit(f"input({password})'s length is not in range: 1 <= len(input) <= 100")
if (not 8 <= len(password) <= 12) and flag:
    print("Invalid")
    flag = False
lowercaseCount = 0
uppercaseCount = 0
digitCount = 0
anythingElse = 0
for char in password:
    if char.isdigit():
        digitCount += 1
    elif char.islower():
        lowercaseCount += 1
    elif char.isupper():
        uppercaseCount += 1
    else:  # char is not digit, not lower, not upper
        anythingElse += 1
        break
if anythingElse > 0 and flag:
    print("Invalid")
    flag = False
if (lowercaseCount < 3 or uppercaseCount < 2 or digitCount < 1) and flag:
    print("Invalid")
    flag = False
if flag: print("Valid")
