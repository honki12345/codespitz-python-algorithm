# USACO 2018 December Contest, Bronze
# Problem 1. Mixing Milk
# https://usaco.org/index.php?page=viewproblem2&cpid=855
input_file = open('mixmilk.in', 'r')
output_file = open('mixmilk.out', 'w')
bucket_capacities = []
milk_amount = []

for i in range(3):
    line = input_file.readline().split()
    if not len(line) == 2:
        exit(f"not {len(line)} == 2")
    if not line[0].isdigit():
        exit(f"not {line[0]} is digit")
    value = int(line[0])
    if not 1 <= value <= 1_000_000_000:
        exit(f"not 1 <= f{value} <= 1_000_000_000")
    bucket_capacities.append(value)
    if not line[1].isdigit():
        exit(f"not {line[1]} is digit")
    value = int(line[1])
    if not 1 <= value <= 1_000_000_000:
        exit(f"not 1 <= f{value} <= 1_000_000_000")
    milk_amount.append(value)
    if not bucket_capacities[i] >= milk_amount[i]:
        exit(f"not {bucket_capacities[i]} >= {milk_amount[i]}")
for i in range(100):
    current_index = i % 3
    next_index = (i + 1) % 3
    if milk_amount[current_index] + milk_amount[next_index] <= bucket_capacities[next_index]:
        milk_amount[next_index] += milk_amount[current_index]
        milk_amount[current_index] = 0
    else:  # milk_amount[current_index] + milk_amount[next_index] > bucket_capacities[next_index]
        move_amount = bucket_capacities[next_index] - milk_amount[next_index]
        milk_amount[next_index] += move_amount
        milk_amount[current_index] -= move_amount


def write_milk_amount(milk_amount, output_file):
    for i in range(len(milk_amount)):
        output_file.write(f"{milk_amount[i]}\n")


write_milk_amount(milk_amount, output_file)
