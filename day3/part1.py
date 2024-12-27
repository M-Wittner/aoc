import sys
from pathlib import Path
import re

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from day1.logger import logger
from day1.part1 import get_file_path_from_user

def extract_functions_by_regex(string: str):
    return re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", string)

def mul(num1, num2):
    # print(num1 * num2)
    return num1 * num2
    

def load_data_from_file(file_path):
    with open(file_path,'r') as input_file:
        lines = []
        for line in input_file:
            lines.append(line.strip())

    return lines
def main():
    file_path = get_file_path_from_user()
    lines = load_data_from_file(file_path)
    total_sum = 0
    for line in lines:
        muls = extract_functions_by_regex(line)
        for mul_str in muls:
            sum = eval(mul_str)
            total_sum += sum
            
    logger.info(f"Total Sum: {total_sum}")
    
    
if __name__ == "__main__":
    main()
