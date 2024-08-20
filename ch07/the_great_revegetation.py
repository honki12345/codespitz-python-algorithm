# USACO 2019 february contest, silver
# problem 3. the great revegetation
# https://usaco.org/index.php?page=viewproblem2&cpid=920

# Main Program
def read_cows(input_file, num_cows):
    """
    inputFile에서 소가 좋아하는 목초지를 읽습니다
    각 소가 좋아하는 목초지들의 리스트를 반환합니다
    리스트 내 각 항목은 한 마리의 소가 가장 좋아하는 두 개의 목초지를 가진 리스트 입니다.

    :param input_file: 읽기 모드로 열려 있는 파일
    :param num_cows: 소들의 수
    :return: 각 소가 좋아하는 목초지들의 리스트
    """
    favorites = []
    for i in range(num_cows):
        lst = input_file.readline().split()
        if not len(lst) == 2:
            exit(f"not {len(lst)} == 2")
        if not lst[0].isdigit:
            exit(f"not {lst[0]} is digit")
        lst[0] = int(lst[0])
        if not 1 <= lst[0] <= 100:
            exit(f"not 1 <= {lst[0]} <= 100")
        if not lst[1].isdigit:
            exit(f"not {lst[1]} is digit")
        lst[1] = int(lst[1])
        if not 1 <= lst[1] <= 111:
            exit(f"not 1 <= {lst[1]} <= 100")
        favorites.append(lst)
    return favorites


def cows_with_favorite(favorites, pasture):
    """
    :param favorites: read_cows 함수가 반환한 각 소가 좋아하는 목초지의 리스트
    :param pasture: 목초지 번호
    :return: 현재 목초지를 좋아하는 소들의 리스트
    """
    cows = []
    for i in range(len(favorites)):
        if favorites[i][0] == pasture or favorites[i][1] == pasture:
            cows.append(i)
    return cows


def types_used(favorites, cows, pasture_types):
    """
    :param favorites: read_cows 함수가 반환한 각 소가 좋아하는 목초지의 리스트
    :param cows: 현재 목초지를 좋아하는 소들의 리스트
    :param pasture_types: 지금까지 각 목초지에 대해 선택된 풀 유형의 리스트
    :return: 소가 좋아하는 목초지를 기반으로 이미 사용된 풀 유형의 리스트를 반환
    """
    used = []
    for cow in cows:
        pasture_a = favorites[cow][0]
        pasture_b = favorites[cow][1]
        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])
        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])
    return used


def smallest_available(used):
    """
    :param used: 사용된 풀 유형들을 담은 리스트
    :return: 사용되지 않은 가장 작은 번호의 풀 유형을 반환
    """
    grass_type = 1
    while grass_type in used:
        grass_type = grass_type + 1
    return grass_type


def write_pastures(output_file, pasture_types):
    """
    :param output_file: 쓰기 모드로 열려있는 파일
    :param pasture_types: 목초지에 심을 풀들의 유형이 정수로 담긴 리스트
    :return:
    """
    pasture_types_str = []
    for pasture_type in pasture_types:
        pasture_types_str.append(str(pasture_type))
    output = ''.join(pasture_types_str)
    output_file.write(output + '\n')


input_file = open('revegetate.in', 'r')
output_file = open('revegetate.out', 'w')

# 입력을 읽는다
lst = input_file.readline().split()
if not len(lst) == 2:
    exit(f"not {len(lst)} == 2")
if not lst[0].isdigit:
    exit(f"not {lst[0]} is digit")
num_pastures = int(lst[0])
if not 2 <= num_pastures <= 100:
    exit(f"not 2 <= {num_pastures} <= 100")
if not lst[1].isdigit:
    exit(f"not {lst[1]} is digit")
num_cows = int(lst[1])
if not 1 <= num_cows <= 150:
    exit(f"not 1 <= {num_cows} <= 150")
favorites = read_cows(input_file, num_cows)

pasture_types = [0]

for i in range(1, num_pastures + 1):
    # 목초지를 좋아하는 소들을 식별한다
    cows = cows_with_favorite(favorites, i)

    # 목초지에 할당할 수 없는 풀 유형을 제거한다
    eliminated = types_used(favorites, cows, pasture_types)

    # 목초지에 심을 가장 작은 번호의 풀 유형을 선택한다
    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)

# 출력을 쓴다
pasture_types.pop(0)
write_pastures(output_file, pasture_types)

input_file.close()
output_file.close()