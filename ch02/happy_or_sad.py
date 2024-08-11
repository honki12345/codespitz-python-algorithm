# ccc15j2 - Happy or Sad
# https://dmoj.ca/problem/ccc15j2
line = input()
if not 1 <= len(line) <= 255:
    exit("input's len is not in range: 1 <= input's len <= 255")
happyEmoticonCount = line.count(":-)")
sadEmoticonCount = line.count(":-(")
if happyEmoticonCount == sadEmoticonCount:
    if happyEmoticonCount == 0:
        print("none")
    else:  # happyEmoticonCount != 0
        print("unsure")
elif happyEmoticonCount > sadEmoticonCount:
    print("happy")
else:  # happyEmoticonCount < sadEmoticonCount
    print("sad")

