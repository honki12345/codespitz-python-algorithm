# ecoo13r1p1 - Take a Number
# https://dmoj.ca/problem/ecoo13r1p1
numberMachine = input()
if not numberMachine.isdigit():
    exit("input is not number")
numberMachine = int(numberMachine)
lateCount = 0
waitCount = 0
while True:
    word = input()
    if not word in ["TAKE", "SERVE", "CLOSE", "EOF"]:
        exit(f"input {word} is not valid (TAKE, SERVE, CLOSE, EOF)")
    if word == "EOF":
        break
    if word == "TAKE":
        waitCount += 1
        lateCount += 1
        numberMachine += 1
    if word == "SERVE":
        waitCount -= 1
    if word == "CLOSE":
        while numberMachine > 999:
            numberMachine -= 999
        print(f"{lateCount} {waitCount} {numberMachine}")
        lateCount = 0
        waitCount = 0
