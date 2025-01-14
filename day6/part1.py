import sys
from pathlib import Path
# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from copy import deepcopy
from day1.logger import logger
from day1.part1 import get_file_path_from_user
from enum import Enum

DIRECTIONS = Enum('Direction', [("^",(-1,0)), (">", (0,1)), ("v",(1,0)), ("<",(0,-1))])

def load_data_from_file(file_path):
    with open(file_path,'r') as input_file:
        lines = []
        for line in input_file:
            lines.append(list(line.strip()))
	
    return lines

def find_starting_position(lines):
    for row in range(len(lines)):
        line = lines[row]
        if "^" in line:
            col = line.index("^")
            return (row, col)


def is_next_step_in_range(point: tuple, crossword_size: int, direction: tuple):
    point_x = deepcopy(point)[1]+direction.value[1]
    point_y = deepcopy(point)[0]+direction.value[0]
    if point_x < 0 or point_x > crossword_size - 1:
        logger.info(f"X ({point_y,point_x}, {direction.name}) out of range {point[0]}+({direction.value[0]})={point_x}, {point_x} < {crossword_size - 1}")
        return False
    if point_y < 0 or point_y > crossword_size - 1:
        logger.info(f"Y ({point_y,point_x}, {direction.name}) out of range {point[1]}+({direction.value[1]})={point_y}, {point_y} < {crossword_size - 1}")
        return False
    logger.info(f"Point {(point_y,point_x), direction.name} is in range {point_x, point_y, crossword_size - 1} - ({point_x < 0 or point_x > crossword_size - 1} or {point_y < 0 or point_y > crossword_size - 1 })")
    return True

def get_next_pos(position, direction):
    return (position[0]+direction.value[0],position[1]+direction.value[1])

def get_next_step(lines, position, direction):
    point_x = deepcopy(position)[1]+direction.value[1]
    point_y = deepcopy(position)[0]+direction.value[0]
    logger.info(f"Fetching step board[{point_y}][{point_x}], {lines[point_y][point_x]}")
    return lines[point_y][point_x]

def get_next_direction(current_direction):
    # print(DIRECTIONS._member_names_.index(current_direction.name))
    direction_names = DIRECTIONS._member_names_
    next_dir_idx = direction_names.index(current_direction.name)+1 if direction_names.index(current_direction.name)+1 < len(DIRECTIONS) else 0
    return DIRECTIONS[direction_names[next_dir_idx]]


def walk_in_direction(board, position, direction):
    # next_step = get_next_step(board, position, direction)
    next_step = board[position[0]+direction.value[0]][position[1]+direction.value[1]]
    logger.info(f"First step is {(position[0]+direction.value[0], position[1]+direction.value[1])} {next_step}")
    # curr_pos = position
    can_walk = True
    while can_walk and next_step != "#":
        can_walk = is_next_step_in_range(position, len(board), direction)
        curr_step = get_next_step(board, position, direction)
        # print("".join(board[position[0]]))
        if curr_step != "#":
            position = get_next_pos(position, direction)
            logger.info(f"Marking board[{position[0]}][{position[1]}] ({board[position[0]][position[1]]}) X")
            board[position[0]][position[1]] = 'X'
            next_step = get_next_step(board, position, direction)
        else:
            break
        logger.info(f"Next pos {direction.name, position, next_step, can_walk}")
    return position

def traverse_board(board, start_pos, direction):
    direction = direction
    curr_pos = start_pos
    can_walk = True
    # i = 0
    while can_walk:
        can_walk = is_next_step_in_range(curr_pos, len(board), direction)
        curr_pos = walk_in_direction(board, curr_pos, direction)
        direction = get_next_direction(direction)
        

    return curr_pos
    
    

def main():
    file_path = get_file_path_from_user()
    lines = load_data_from_file(file_path)
    board_copy = deepcopy(lines)
    starting_position = find_starting_position(board_copy)
    current_direction = DIRECTIONS["^"]
    traverse_board(board_copy, starting_position, current_direction)
    
    x_count = 0
    for line in board_copy:
        x_count += line.count('X')
        print("".join(line))
    print('-----------------------------------')
    for line in lines:
        # x_count += line.count('X')
        print("".join(line))
    logger.info(f"Total Unique Paths crossed: {x_count}")
    
    
if __name__ == "__main__":
    main()



# get starting position and direction
# check if next position(direction) is in range
# if in range, check if path is clear (not #)
# if so, walk in that direction until reaching end of path - #
# in every step mark the prevoius one with X
# if reached end of path, turn 90 right and do all again
# count how many X in new board