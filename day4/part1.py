import sys
from pathlib import Path
import re
from copy import deepcopy
from enum import Enum

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from day1.logger import logger
from day1.part1 import get_file_path_from_user

def load_data_from_file(file_path):
    with open(file_path,'r') as input_file:
        lines = []
        for line in input_file:
            lines.append(line.strip())
	
    return lines
# 8 directions: Forward, bottom right, down, bottom left, backward, top left, up, top right
#               (0,1)       (1,1)     (1,0)    (-1,-1)      (0,-1)  (-1,-1) (-1,0) (-1,1)
# DIRECTIONS = [(0,1),(1,1),(1,0),(-1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
DIRECTIONS = Enum('Direction', [("Forward", (1,0)), ("Bottom_Right",(1,1)), ("Down",(0,1)), ("Bottom_Left",(-1,1)), ("Backward",(-1,0)), ("Top_Left",(-1,-1)), ("Up",(0,-1)), ("Top_Right",(1,-1))])

def can_check_direction(point: tuple, word_length: int, crossword_size: int, direction: tuple):
    # for i in range(word_length):
    point_x = deepcopy(point)[0]+(direction.value[0]*word_length)
    point_y = deepcopy(point)[1]+(direction.value[1]*word_length)
    if point_x < 0 or point_x > crossword_size-1:
        logger.info(f"X ({point}, {direction.name}) out of range ({point_x},{point_y})")
        return False
    if point_y < 0 or point_y > crossword_size-1:
        logger.info(f"Y ({point}, {direction.name}) out of range ({point_x},{point_y})")
        return False
    logger.info(f"Point {point, direction.name} is in range {point_x, point_y, crossword_size} - ({point_x < 0 or point_x > crossword_size-1} or {point_y < 0 or point_y > crossword_size-1})")
    return True

def check_direction(point, direction, word, crossword):
    point_copy = deepcopy(point)
    
    for i in range(len(word)):
        logger.info(f"#{i} Checking Point {point_copy, direction.value}, word {word[i]} cross {crossword[point_copy[1]][point_copy[0]]}")
        if word[i] != crossword[point_copy[1]][point_copy[0]]:
            return False
        point_copy = (point_copy[0]+direction.value[0], point_copy[1]+direction.value[1])
    
    return True
        
def solve_crossword(lines):
    xmas = "XMAS"
    word_length = len(xmas)
    logger.info(word_length)
    crossword_size = len(lines) # assuming this is an even dimensioned crossword
    count = 0
    for l in range(len(lines)):
        line = lines[l]
        point_y = l
        for i in range(len(line)):
            point_x = i
            point = (point_x, point_y)
            if line[i] != xmas[0]:
                logger.info(f"Word doesn't start with {line[i]} Skipping {point}")
                continue
            logger.info(f"Point: {point}, letter: {line[i]}")
            for direction in DIRECTIONS:
                # logger.info(direction.name)
                if can_check_direction(point, word_length, crossword_size, direction):
                    if check_direction(point, direction, xmas, lines):
                        count += 1
                        logger.info(f"Found match #{count}! {point, direction.name}")

    return count

def main():
    file_path = get_file_path_from_user()
    lines = load_data_from_file(file_path)
    
    count = solve_crossword(lines)
    logger.info(count)

if __name__ == "__main__":
    main()


# (?(?=X).|)(?(?=M).|)(?=A).(?=S).|(?=S).(?=A).(?=M).(?=X).