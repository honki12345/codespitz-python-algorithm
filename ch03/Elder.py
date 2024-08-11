# coci18c4p1 - Elder
# https://dmoj.ca/problem/coci18c4p1
wizardWandObeyed = input()
if not wizardWandObeyed.isupper():
    exit(f"input({wizardWandObeyed}) is not upper")
battleCount = input()
if not battleCount.isdigit():
    exit(f"input({battleCount}) is not number")
battleCount = int(battleCount)
obeyedCount = 1
if not 1 <= battleCount <= 100:
    exit(f"input({battleCount}) is not in range: 1 <= input <= 100")
for i in range(battleCount):
    line = input()
    winner = line[0]
    if not winner.isupper():
        exit(f"input({winner}) is not upper")
    loser = line[2]
    if not loser.isupper():
        exit(f"input({loser}) is not upper")
    if loser == wizardWandObeyed[-1]:
        if not (winner in wizardWandObeyed):
            obeyedCount += 1
        wizardWandObeyed += winner
print(wizardWandObeyed[-1])
print(obeyedCount)
