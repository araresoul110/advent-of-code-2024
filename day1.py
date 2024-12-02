from prep_input import *

def compare_lists(part):

    total = 0
    numbers_l = []
    numbers_r = []
    Lines = prep_input('day1_input.txt')

    for line in Lines:
        split_line = line.split("   ")
        numbers_l.append(split_line[0])
        numbers_r.append(split_line[1])

    if (part == 1):
        numbers_l.sort()
        numbers_r.sort()

        for idx, pair in enumerate(numbers_l):
            total += abs(int(numbers_l[idx]) - int(numbers_r[idx]))
    else:
        for locationId in numbers_l:
            idCount = numbers_r.count(locationId)
            total += idCount * int(locationId)

    return total

solution = compare_lists(2)
print(solution)
# Solution:
#  1603498
#  25574739
