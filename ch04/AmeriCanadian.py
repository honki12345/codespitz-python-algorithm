# ccc02j2 - AmeriCanadian
# https://dmoj.ca/problem/ccc02j2
while True:
    word = input()
    if len(word) > 64:
        exit("input not to exceed 64 letters")
    if word == "quit!":
        break
    if len(word) > 4 and \
            not word[-3] in "aeiouy" and\
            word[-2] == 'o' and word[-1] == 'r':
        word = word[:-2] + "our"
    print(word)


