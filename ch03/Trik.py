# coci06c5p1 - Trik
# https://dmoj.ca/problem/coci06c5p1
moves = input()
if not moves.count('A') + moves.count('B') + moves.count('C') == len(moves):
    exit(f"input({moves} not consist of A B C")
cups = "ABC"
for char in moves:
    if char == 'A':
        cups = cups[1] + cups[0] + cups[2]
    elif char == 'B':
        cups = cups[0] + cups[2] + cups[1]
    else:  # char == 'C'
        cups = cups[2] + cups[1] + cups[0]
print(cups.find('A') + 1)
