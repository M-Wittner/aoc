import sys
from pathlib import Path
# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import math
import re
from operator import itemgetter
from day1.logger import logger
from day1.part1 import get_file_path_from_user
from part1 import load_data_from_file, is_update_valid

def get_mid_page(update):
    middle_num = int(update[math.floor(len(update)/2)])
    logger.info(
        f"Middle of {update} at index {math.floor(len(update)/2)}/{len(update)} is {middle_num}")
    return middle_num

def fix_update(update, rules):
    update_rules = []
    fixed_update = []
    for rule in rules:
        if set([rule[0], rule[1]]).issubset(update):
            update_rules.append(rule)
    
    sorted_rules = sorted(update_rules, key=itemgetter(0, 1), reverse=True)
    logger.info(f"update {update}")
    logger.info(f"sorted_rules {sorted_rules}")
    
    for rule in sorted_rules:
        if not update.index(rule[0]) < update.index(rule[1]):
            logger.info(f"update NOT Follow Rule {rule}")
            left = update[update.index(rule[0])]
            left_i = update.index(rule[0])
            right_i = update.index(rule[1])
            right = update[update.index(rule[1])]
            update[right_i] = left
            del update[left_i]
            update.insert(right_i+1, right)
    
    logger.info(f"Fixed: {update}")
    return update


def main():
    file_path = get_file_path_from_user()
    rules, updates = load_data_from_file(file_path)
    valid_updates = []
    total_sum = 0

    for update in updates:

        if is_update_valid(update, rules):
            valid_updates.append(update)
            logger.info(f"Update is Valid!")
        else:
            fixed_update = fix_update(update.copy(), rules)
            if is_update_valid(fixed_update, rules):
                valid_updates.append(fixed_update)
                logger.info(f"Update fix is Valid!")
                middle_num = get_mid_page(fixed_update)
                total_sum += middle_num

    logger.info(
        f"Total Valid Updates: {len(valid_updates)}, Summed middle pages: {total_sum}")


if __name__ == "__main__":
    main()
