# ccc18j1 - Telemarketer or not?
# https://dmoj.ca/problem/ccc18j1

lastFourDigits = ""
result = ""
for i in range(4):
    number = input()
    if not number.isdigit():
        exit(f"input({number}) is not number")
    lastFourDigits += number
if not (lastFourDigits[0] == '8' or lastFourDigits[0] == '9'):
    result = "answer"
if not (lastFourDigits[-1] == '8' or lastFourDigits[-1] == '9') and result != "answer":
    result = "answer"
if not (lastFourDigits[1] == lastFourDigits[2]) and result != "answer":
    result = "answer"
if result == "answer":
    print("answer")
else:  # result != "answer"
    print("ignore")