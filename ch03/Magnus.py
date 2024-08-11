# coci18c3p1 - Magnus
# https://dmoj.ca/problem/coci18c3p1
word = input()
if not 1 <= len(word) <= 100000:
    exit(f"input({word}'s len is not in range: 1 <= input's len <= 100000")
block = "HONI"
blockIdx = 0
subWordCount = 0
for char in word:
    if char == block[blockIdx]:
        blockIdx = (blockIdx + 1) % len(block)
        if blockIdx == 0:
            subWordCount += 1
print(subWordCount)
