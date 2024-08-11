# (wc15c2j1) A New Hope
# https://dmoj.ca/problem/wc15c2j1

N = input()
if not N.isdigit():
    exit("N is not integer")
N = int(N)
if not 1 <= N <= 5:
    exit("not 1 <= N <= 5")
prefix = "A long time ago in a galaxy "
repeatingWord = "far, " * (N - 1) + "far "
suffix = "away..."
print(prefix + repeatingWord + suffix)
