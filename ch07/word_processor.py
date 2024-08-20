# USACO 2020 january contest, bronze
# problem 1. word processor
# https://usaco.org/index.php?page=viewproblem2&cpid=987
input_file = open('word.in', 'r')
output_file = open('word.out', 'w')

lst = input_file.readline().split()
if not len(lst) == 2:
    exit(f"not {len(lst)} == 2")
if not lst[0].isdigit():
    exit(f"not {lst[0]} is digit")
word_count = int(lst[0])
if not 1 <= word_count <= 100:
    exit(f"not 1 <= {word_count} <= 100")
if not lst[1].isdigit():
    exit(f"not {lst[1]} is digit")
characters_count = int(lst[1])
if not 1 <= characters_count <= 80:
    exit(f"not 1 <= {characters_count} <= 80")
words = input_file.readline().split()
if not len(words) == word_count:
    exit(f"not {len(words)} == {word_count}")

line = ''
chars_on_line = 0

for word in words:
    if chars_on_line + len(word) <= characters_count:
        line = line + word + ' '
        chars_on_line = chars_on_line + len(word)
    else:  # charsOnLine + len(word) > charactersCount
        output_file.write(line[:-1] + '\n')
        line = word + ' '
        chars_on_line = len(word)
output_file.write(line[:-1] + '\n')

input_file.close()
output_file.close()
