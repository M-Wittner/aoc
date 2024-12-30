import sys
from pathlib import Path
import re
from collections import Counter

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from day1.logger import logger
from day1.part1 import get_file_path_from_user

def load_data_from_file(file_path):
    with open(file_path,'r') as input_file:
        lines = []
        columns = []
        for line in input_file:
            lines.append(line.strip())
            for i in range(len(line)-1):
                if len(columns) <= i:
                    columns.insert(i,"")
                columns[i] = f"{columns[i]}{line[i]}"
	
    return lines, columns

# def load_data_from_file(path):
#     string = None
#     with open(path, 'r') as file:
#         string = file.read().replace('\n', '')
#     return string

def re_sreach(string):
    matches = re.findall(r"XMAS|SAMX", string)

    # print(f"found {matches} in {string}")
    match_strings = []
    for match in matches:
        match_strings.append(match[0] or match[1])
    return len(match_strings)

# def re_search(string, pattern):
#     search_pattern = '.*'.join(list(pattern))
#     print(f"Looking for {pattern} in {string}")
#     obj = re.compile(search_pattern)
#     return obj.search(string)

# def find_xmases(string: str):
#     xmas = "XMAS"
#     samx = "SAMX"
#     count = 0
#     if re_search(string, xmas):
#         count +=1
#     if re_search(string, samx):
#         count +=1
#     print(f"found {count}")
#     return count

def crossword(lines):
    xmas = "XMAS"
    samx = "SAMX"
    count = 0
    
    for l in range(len(lines)-1):
        line = lines[l]
        for i in range(len(line)-5):
            letter = line[i]
            if letter == xmas[0] or letter == samx[0]:
                word = line[i:i+4]
                # cross_word = [line[i],lines[l+1][i+1]]
                cross_word = "".join([line[i]]+ [lines[l+1+s][i+1+s] for s in range(len(line)-i-1-l)])
                cross_matches = re_sreach(cross_word)
                print(f"Line #{l+1} CrossWord [#{i+1}]: {cross_word} in line {line}, matched {cross_matches}")
                # reverse_cross_word = "".join([line[i]]+ [lines[l+1+s][i-1-s] for s in range(i)])
                # reverse_cross_matches = re_sreach(reverse_cross_word)
                # print(f"Line #{l+1} Revered CrossWord [#{i+1}]: {reverse_cross_word} in line {line}, matched {reverse_cross_matches}")
                if word == xmas or word == samx:
                    print(f"Word: {word} in line {line}")
                    count += 1
                count += cross_matches #+reverse_cross_matches
    return count

# def check_diagnols(lines):
#     for line in lines:
#         for letter in

def main():
    file_path = get_file_path_from_user()
    lines, columns = load_data_from_file(file_path)
    # text = load_data_from_file(file_path)
    xmases = 0
    xmases = crossword(lines) + crossword(columns)
    # xmases = find_xmases(text)
    # for line in lines:
    #     xmases += find_xmases(line)
    # for col in columns:
    #     xmases += find_xmases(col)
    
    print(xmases)

if __name__ == "__main__":
    main()


# (?(?=X).|)(?(?=M).|)(?=A).(?=S).|(?=S).(?=A).(?=M).(?=X).