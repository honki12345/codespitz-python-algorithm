# 2144 - cleaning the room
# https://acm.timus.ru/problem.aspx?space=1&num=2144
def is_sorted(box_list):
    for j in range(len(box_list)):
        max_size = 0
        for k in range(len(box_list[j])):
            size = box_list[j][k]
            if size >= max_size:
                max_size = size
            else:  # size < maxSize
                return False
    return True


def can_clean(box_list):
    end_size = 0
    for j in range(len(box_list)):
        start_size = box_list[j][0]
        if end_size > start_size:
            return False
        end_size = box_list[j][-1]
    return True


boxCount = input().strip()
if not boxCount.isdigit():
    exit(f"not {boxCount} is digit")
boxCount = int(boxCount)
if not 1 <= boxCount <= 100:
    exit(f"not 1 <= {boxCount} <= 100")
boxes = []
for _ in range(boxCount):
    boxInfo = input().strip().split(" ")
    if not len(boxInfo) > 0:
        exit(f"not {len(boxInfo)} > 0")
    boxLength = boxInfo[0]
    if not boxLength.isdigit():
        exit(f"not {boxLength} is digit")
    boxLength = int(boxLength)
    if not len(boxInfo) == boxLength + 1:
        exit(f"not {len(boxInfo)} == {boxLength + 1}")
    box = []
    for i in range(1, len(boxInfo)):
        if not boxInfo[i].isdigit():
            exit(f"not {boxInfo[i]} is digit")
        value = int(boxInfo[i])
        if not 1 <= value <= 10 ** 4:
            exit(f"not 1 <= {value} <= 10 ** 4")
        box.append(value)
    boxes.append(box)
boxes.sort()
if is_sorted(boxes) and can_clean(boxes):
    print("YES")
else:  # not is_sorted() or not can_clean()
    print("NO")

