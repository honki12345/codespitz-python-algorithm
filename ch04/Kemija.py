# coci08c3p2 - Kemija
# https://dmoj.ca/problem/coci08c3p2
codedSentence = input()
if not codedSentence.islower():
    exit("sentence consists only of lowercase letters")
if not len(codedSentence) <= 100:
    exit("total number of characters will be at most 100")
if codedSentence[0] == ' ' or codedSentence[-1] == ' ':
    exit("no leading or trailing spaces")
if codedSentence.count('  ') != 0 or codedSentence.count('   ') != 0:
    exit("separated by exactly one space")

idx = 0
decodedSentence = ""
while idx < len(codedSentence):
    decodedSentence += codedSentence[idx]
    if codedSentence[idx] == 'a' or codedSentence[idx] == 'e' \
            or codedSentence[idx] == 'i' or codedSentence[idx] == 'o'\
            or codedSentence[idx] == 'u':
        idx += 3
    else:  # codeSentence[idx] is not vowel
        idx += 1
print(decodedSentence)
