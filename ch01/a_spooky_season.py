# (wc16c1j1) A Spooky Season
# https://dmoj.ca/problem/wc16c1j1

S = input()

if not S.isdigit():
    exit("S is not integer")
S = int(S)

if not 2 <= S <= 20:
    exit("not 2 <= S <= 20")

output = "sp" + ("o" * S) + "ky"
print(output)
