import math
from prep_input import *

def check_safety(part):

    total = 0
    Lines = prep_input('day2_input.txt')

    for line in Lines:
        split_line = line.split(" ")
        int_line = [int(x) for x in split_line]

        if (all(i < j for i, j in zip(int_line, int_line[1:])) == True or all(i > j for i, j in zip(int_line, int_line[1:])) == True) and (all(abs(j - i) < 4 for i, j in zip(int_line, int_line[1:])) == True):
            total += 1
        elif (part == 2):
            for idx, element in enumerate(int_line):
                test_line = int_line.copy() 
                del test_line[idx]
                if (all(i < j for i, j in zip(test_line, test_line[1:])) == True or all(i > j for i, j in zip(test_line, test_line[1:])) == True) and (all(abs(j - i) < 4 for i, j in zip(test_line, test_line[1:])) == True):
                    total += 1
                    break

    return total

solution = check_safety(2)
print(solution)
# Solution:
#  369
#  428