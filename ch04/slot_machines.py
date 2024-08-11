# ccc00s1 - Slot Machines
# https://dmoj.ca/problem/ccc00s1
quarters = input()
if not quarters.isdigit():
    exit(f"quarters 입력 값 {quarters}이 숫자가 아닙니다")
quarters = int(quarters)
if not 1 <= quarters < 1000:
    exit(f"quarters 입력 값 {quarters}이 1 이상 1000 미만이 아닙니다")
firstMachinePlayedTime = input()
if not firstMachinePlayedTime.isdigit():
    exit(f"firstMachinePlayedTime 입력 값 {firstMachinePlayedTime}이 숫자가 아닙니다")
firstMachinePlayedTime = int(firstMachinePlayedTime)
if not firstMachinePlayedTime >= 0:
    exit(f"firstMachinePlayedTime 입력 값 {firstMachinePlayedTime}이 0 보다 크거나 같지 않습니다")
secondMachinePlayedTime = input()
if not secondMachinePlayedTime.isdigit():
    exit(f"secondMachinePlayedTime 입력 값 {secondMachinePlayedTime}이 숫자가 아닙니다")
secondMachinePlayedTime = int(secondMachinePlayedTime)
if not secondMachinePlayedTime >= 0:
    exit(f"secondMachinePlayedTime 입력 값 {secondMachinePlayedTime}이 0 보다 크거나 같지 않습니다")
thirdMachinePlayedTime = input()
if not thirdMachinePlayedTime.isdigit():
    exit(f"thirdMachinePlayedTime 입력 값 {thirdMachinePlayedTime}이 숫자가 아닙니다")
thirdMachinePlayedTime = int(thirdMachinePlayedTime)
if not thirdMachinePlayedTime >= 0:
    exit(f"thirdMachinePlayedTime 입력 값 {thirdMachinePlayedTime}이 0 보다 크거나 같지 않습니다")

machineIdx = 0
while quarters > 0:
    if machineIdx % 3 == 0:
        firstMachinePlayedTime += 1
        if firstMachinePlayedTime % 35 == 0:
            quarters += 30
    elif machineIdx % 3 == 1:
        secondMachinePlayedTime += 1
        if secondMachinePlayedTime % 100 == 0:
            quarters += 60
    else: # machineIdx % 3 == 2
        thirdMachinePlayedTime += 1
        if thirdMachinePlayedTime % 10 == 0:
            quarters += 9
    machineIdx += 1
    quarters -= 1
print(f"Martha plays {machineIdx} times before going broke.")
