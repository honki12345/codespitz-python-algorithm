# ccc08j2 - Do the Shuffle
# https://dmoj.ca/problem/ccc08j2
playList = "ABCDE"
while True:
    buttonNumber = input()
    if not buttonNumber.isdigit():
        exit(f"input {buttonNumber} is not number")
    buttonNumber = int(buttonNumber)
    if not 1 <= buttonNumber <= 4:
        exit(f"input {buttonNumber} is not in range: 1 <= b <= 4")
    times = input()
    if not times.isdigit():
        exit(f"input {times} is not number")
    times = int(times)
    if not 1 <= times <= 10:
        exit(f"input {times} is not in range: 1 <= times <= 10")
    if buttonNumber == 1:
        while times > 0:
            playList = playList[1] + playList[2] + playList[3] + playList[4] + playList[0]
            times -= 1
    elif buttonNumber == 2:
        while times > 0:
            playList = playList[4] + playList[0] + playList[1] + playList[2] + playList[3]
            times -= 1
    elif buttonNumber == 3:
        while times > 0:
            playList = playList[1] + playList[0] + playList[2] + playList[3] + playList[4]
            times -= 1
    else:  # buttonNumber == 4:
        print(playList[0] + ' ' + playList[1] + ' ' + playList[2] + ' ' + playList[3] + ' ' + playList[4])
        break
