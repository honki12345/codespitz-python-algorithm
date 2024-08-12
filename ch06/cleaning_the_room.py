# 2144 - cleaning the room
# https://acm.timus.ru/problem.aspx?space=1&num=2144
boxCount = input().strip()
if not boxCount.isdigit():
    exit(f"not {boxCount} is digit")
boxCount = int(boxCount)
if not 1 <= boxCount <= 100:
    exit(f"not 1 <= {boxCount} <= 100")
boxes = []
for _ in range(boxCount):
    boxInfo = input().strip().split(" ")
    boxLength = boxInfo[0]
    if not boxLength.isdigit():
        exit(f"not {boxLength} is digit")
    boxLength = int(boxLength)
    if not len(boxInfo) == boxLength + 1:
        exit(f"not {len(boxInfo)} == {boxLength + 1}")
    maxSize = 0
    box = []
    for i in range(1, len(boxInfo)):
        if not boxInfo[i].isdigit():
            exit(f"not {boxInfo[i]} is digit")
        value = int(boxInfo[i])
        if not 1 <= value <= 10 ** 4:
            exit(f"not 1 <= {value} <= 10 ** 4")
        if value >= maxSize:
            maxSize = value
        else:  # value < maxSize
            print("NO")
            exit()
        box.append(value)
    box.sort()
    boxes.append(box)
boxes.sort()
endSize = 0
canClean = True
for i in range(len(boxes)):
    startSize = boxes[i][0]
    if endSize > startSize:
        canClean = False
        break
    endSize = boxes[i][-1]
if canClean:
    print("YES")
else:  # canClean == False
    print("NO")

