# (ccc13j1) Next in Line
# https://dmoj.ca/problem/ccc13j1
Y = input()
if not Y.isdigit():
    exit("input is not integer")
YoungestChildAge = int(Y)
if not 0 <= YoungestChildAge <= 50:
    exit("age is not 0 <= age <= 50")

M = input()
if not M.isdigit():
    exit("input is not integer")
MiddleChildAge = int(M)
if not YoungestChildAge <= MiddleChildAge <= 50:
    exit("age is not YoungestChildAge <= age <= 50")

if not MiddleChildAge >= YoungestChildAge:
    exit("MiddleChildAge is not greater than YoungestChildAge")

gap = MiddleChildAge - YoungestChildAge
OldestChildAge = MiddleChildAge + gap
print(OldestChildAge)
