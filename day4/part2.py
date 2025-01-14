import sys
from pathlib import Path
from copy import deepcopy
from enum import Enum

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from logger import logger, solution_logger
from day1.part1 import get_file_path_from_user
from part1 import can_check_direction

def load_data_from_file(file_path):
    with open(file_path,'r') as input_file:
        lines = []
        for line in input_file:
            lines.append(line.strip())
	
    return lines

DIRECTIONS = Enum('Direction', [("Top_Left",(-1,-1)), ("Bottom_Right",(1,1)), ("Top_Right",(1,-1)), ("Bottom_Left",(-1,1))])


def get_point_in_direction(point, direction, crossword):
    point_copy = deepcopy(point)
    point_x = point_copy[0]+direction.value[0]
    point_y = point_copy[1]+direction.value[1]
    # logger.info(f"Point {point_copy, crossword[point[1]][point[0]]} in direction {direction.name} is ({point_x}, {point_y} - {crossword[point_y][point_x]})")
    return crossword[point_y][point_x]
    

def check_x_direction(point, word, crossword):
    point_copy = deepcopy(point)
    
    top_left = get_point_in_direction(point_copy, DIRECTIONS['Top_Left'], crossword)
    top_right = get_point_in_direction(point_copy, DIRECTIONS['Top_Right'], crossword)
    bottom_left = get_point_in_direction(point_copy, DIRECTIONS['Bottom_Left'], crossword)
    bottom_right = get_point_in_direction(point_copy, DIRECTIONS['Bottom_Right'], crossword)
    middle = crossword[point[1]][point[0]]
    diag_1 = "".join([top_left, middle, bottom_right])
    diag_2 = "".join([top_right, middle, bottom_left])
    diag_3 = "".join([bottom_right, middle, top_left])
    diag_4 = "".join([bottom_left, middle, top_right])

    match_letters = [word[0],word[-1]]
    if ((top_left == top_right and bottom_left == bottom_right) or (top_right == bottom_right and top_left == bottom_left)):
        if all(p in match_letters for p in [top_left, top_right, bottom_left, bottom_right]):
            # if ("".join([top_left, middle, bottom_right]) == word[::-1]):
            logger.info(f"{diag_1}, {diag_2}, {diag_3}, {diag_4}")
            logger.info(f"Found match! {point} {top_left,top_right,bottom_left,bottom_right}, {all(p in match_letters for p in [top_left, top_right, bottom_left, bottom_right])}")
            logger.info(f"{top_left} . {top_right}")
            logger.info(f"  {middle}  ")
            logger.info(f"{bottom_left} . {bottom_right}")
            return True
    solution_logger.info('.')
    return False

def solve_crossword(lines):
    word = "MAS"
    logger.error(word[::-1])
    word_length = int((len(word)-1)/2)
    logger.info(word_length)
    crossword_size = len(lines)-1 # assuming this is an even dimensioned crossword
    # solution_board = [['.']*len(lines) for i in range(len(lines))]
    # print(solution_board)
    logger.info(f"Cross Size {crossword_size}")
    count = 0
    for l in range(word_length, len(lines)):
        line = lines[l]
        point_y = l
        for i in range(word_length, len(line)):
            point_x = i
            point = (point_x, point_y)
            if line[i] != word[1]:
                logger.info(f"{point} X of MAS doesn't start with {line[i]} Skipping")
                if line[i] not in word:
                    # solution_board[l][i] = '.'
                    solution_logger.info('.')
                # else:
                #     solution_logger.info(line[i])
                continue
            logger.info(f"Point: {point}, letter: {line[i]}")
            check_x = True
            for direction in DIRECTIONS:
                if not can_check_direction(point, word_length, crossword_size, direction):
                    logger.info(f"{point} - Can't Check X")
                    check_x = False
                    break
            
            if check_x:
                logger.info(f"{point} - Can Check X")
                if check_x_direction(point, word, lines):
                    count += 1
                else:
                    solution_logger(line[i])
        solution_logger.info('\n')
    # logger.info(solution_board)
    return count
        
def main():
    file_path = get_file_path_from_user()
    lines = load_data_from_file(file_path)
    
    # check_x_direction(lines, 'MAS', lines)
    count = solve_crossword(lines)
    logger.info(count)

if __name__ == "__main__":
    main()
