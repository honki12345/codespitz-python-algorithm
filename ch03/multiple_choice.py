# ccc11s2 - Multiple Choice
# https://dmoj.ca/problem/ccc11s2
problemCount = input()
if not problemCount.isdigit():
    exit(f"input({problemCount}) is not number")
problemCount = int(problemCount)
if not 0 < problemCount < 10000:
    exit(f"input({problemCount}) is not in range: 0 < input < 10000")
studentAnswer = ""
for i in range(problemCount):
    answer = input()
    if not (answer in "ABCDE"):
        exit(f"input({answer}) is not A B C D E")
    studentAnswer += answer
problemAnswer = ""
for i in range(problemCount):
    answer = input()
    if not (answer in "ABCDE"):
        exit(f"input({answer}) is not A B C D E")
    problemAnswer += answer
score = 0
for i in range(problemCount):
    if studentAnswer[i] == problemAnswer[i]:
        score += 1
print(score)
