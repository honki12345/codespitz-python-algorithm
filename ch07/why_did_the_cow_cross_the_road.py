# USACO 2017 February Contest, Bronze
# Problem 1. Why Did the Cow Cross the Road
# https://usaco.org/index.php?page=viewproblem2&cpid=711
def check_position(cow_id, cow_positions_copy, position, crossings_number):
    previous_position = cow_positions_copy[cow_id]
    if previous_position == -1:
        cow_positions_copy[cow_id] = position
    else:  # previous_position != -1
        if previous_position != position:
            crossings_number += 1
            cow_positions_copy[cow_id] = position
    return crossings_number, cow_positions_copy


input_file = open('crossroad.in', 'r')
output_file = open('crossroad.out', 'w')
first_line = input_file.readline().strip()
if not first_line.isdigit():
    exit(f"not {first_line} is digit")
observations_number = int(first_line)
if not 1 <= observations_number <= 100:
    exit(f"not 1 <= {observations_number} <= 100")
crossings_number = 0
cow_positions = [-1] * 11
for _ in range(observations_number):
    line = input_file.readline().split()
    if not len(line) == 2:
        exit(f"not {len(line)} == 2")
    if not line[0].isdigit():
        exit(f"not {line[0]} is digit")
    cow_id = int(line[0])
    if not 1 <= cow_id <= 10:
        exit(f"not 1 <= {cow_id} <= 10")
    if not (line[0].isdigit()):
        exit(f"not {line[1]} is digit")
    position = int(line[1])
    if not (position == 0 or position == 1):
        exit(f"not {position} == 0 or == 1")
    crossings_number, cow_positions \
        = check_position(cow_id, cow_positions[:], position, crossings_number)
output_file.write(f"{str(crossings_number)}")
