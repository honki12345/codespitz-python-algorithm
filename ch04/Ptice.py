# coci08c1p2 - Ptice
# https://dmoj.ca/problem/coci08c1p2
numberQuestions = input()
if not numberQuestions.isdigit():
    exit(f"input {numberQuestions} is not digit")
numberQuestions = int(numberQuestions)
if not 1 <= numberQuestions <= 100:
    exit(f"input {numberQuestions} is not in range: 1 <= input <= 100")
correctAnswer = input()
if not correctAnswer.count('A') + correctAnswer.count('B') + correctAnswer.count('C') == len(correctAnswer):
    exit(f"input {correctAnswer} is not consists of ABC")

answers = ["ABC", "BABC", "CCAABB"]
scores = [0, 0, 0]
names = ["Adrian", "Bruno", "Goran"]
for i in range(len(correctAnswer)):
    for j in range(len(names)):
        if correctAnswer[i] == answers[j][i % len(answers[j])]:
            scores[j] += 1
maxScore = 0
maxScorenames = ""
for i in range(len(scores)):
    if maxScore < scores[i]:
        maxScore = scores[i]
        maxScorenames = names[i]
    else:  # maxScore >= scores[i]
        if maxScore == scores[i]:
            if i == 0:
                maxScorenames = names[i]
            else:
                maxScorenames = maxScorenames + "\n" + names[i]

print(maxScore)
print(maxScorenames)