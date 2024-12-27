import sys
from pathlib import Path
import re

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from day1.logger import logger
from day1.part1 import get_file_path_from_user
from part1 import mul, extract_functions_by_regex

def extract_doables(string: str):
    matches = re.findall(r"^(.*?)(?=don't\(\))|(?<=do\(\))(.*?)(?=don't\(\)|$)", string)
    match_strings = []
    for match in matches:
        match_strings.append(match[0] or match[1])
    return match_strings

def load_data_from_file(path):
    string = None
    with open(path, 'r') as file:
        string = file.read().replace('\n', '')
    return string
        
def main():
    file_path = get_file_path_from_user()
    content = load_data_from_file(file_path)
    total_sum = 0
    doables = extract_doables(content)
    for doable in doables:
        muls = extract_functions_by_regex(doable)
        for mul_str in muls:
            sum = eval(mul_str)
            total_sum += sum
            
    logger.info(f"Total Sum: {total_sum}")
    
    
if __name__ == "__main__":
    main()
