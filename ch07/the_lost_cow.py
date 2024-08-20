# USACO 2017 US Open Contest, Bronze
# Problem 1. The Lost Cow
# https://usaco.org/index.php?page=viewproblem2&cpid=735
def get_move_times(position_x, position_y):
    origin_position_x = position_x
    previous_position_x = position_x
    move_distances = 1
    total_moved_distances = 0
    loop_limitations = 100_000
    while loop_limitations > 0:
        moved_position_x = origin_position_x + move_distances
        if moved_position_x > 0 and position_y > 0 and moved_position_x > position_y:
            total_moved_distances += abs(previous_position_x - position_y)
            break
        elif moved_position_x < 0 and position_y < 0 and moved_position_x < position_y:
            total_moved_distances += abs(previous_position_x - position_y)
            break
        else:  # distances와 move_distances가 부호가 다르거나, 같으면서 절대값 크기가 같지 않을 때
            total_moved_distances += abs(previous_position_x - moved_position_x)
            move_distances *= -2
        loop_limitations -= 1
        previous_position_x = moved_position_x
    return total_moved_distances


input_file = open('lostcow.in', 'r')
output_file = open('lostcow.out', 'w')
line = input_file.readline().split()
if not len(line) == 2:
    exit(f"not {len(line)} == 2")
if not line[0].isdigit():
    exit(f"not {line[0]} is digit")
position_x = int(line[0])
if not 0 <= position_x <= 1000:
    exit(f"not 0 <= {position_x} <= 1000")
position_y = int(line[1])
if not 0 <= position_y <= 1000:
    exit(f"not 0 <= {position_y} <= 1000")
distances = position_x - position_y
if distances == 0:
    output_file.write("0")
else:  # distances != 0
    total_moved_distances = get_move_times(position_x, position_y)
    output_file.write(str(total_moved_distances))

