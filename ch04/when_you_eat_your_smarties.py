# ecoo15r1p1 - When You Eat Your Smarties
# https://dmoj.ca/problem/ecoo15r1p1
for i in range(10):
    counts = [0, 0, 0, 0, 0, 0, 0, 0]
    totalTime = 0
    while True:
        color = input()
        if not (color in ["orange", "blue", "green", "yellow", "pink", "violet", "brown", "red"] or
                color == "end of box"):
            exit(f"input({color}) is not valid (not colors, not end condition)")
        if color == "orange":
            counts[0] += 1
        elif color == "blue":
            counts[1] += 1
        elif color == "green":
            counts[2] += 1
        elif color == "yellow":
            counts[3] += 1
        elif color == "pink":
            counts[4] += 1
        elif color == "violet":
            counts[5] += 1
        elif color == "brown":
            counts[6] += 1
        elif color == "red":
            counts[7] += 1
        else:  # color == "end of box"
            for j in range(len(counts)):
                if j != len(counts) - 1:  # color is not red
                    totalTime += ((counts[j] - 1) // 7 + 1) * 13  # [1:7) -> 1, [8:14) -> 2, [15:21) -> 3
                else:  # color is red
                    totalTime += counts[j] * 16
            print(totalTime)
            break
