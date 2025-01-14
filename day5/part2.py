import sys
from pathlib import Path
# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import math
import re
from operator import itemgetter
from day1.logger import logger
from day1.part1 import get_file_path_from_user
from part1 import load_data_from_file

def is_update_valid(update, rules):
    update_rules = []
    for rule in rules:
        if not set([rule[0], rule[1]]).issubset(update):
            continue
        if not update.index(rule[0]) < update.index(rule[1]):
            return False
        update_rules.append(rule)

    sorted_rules = sorted(update_rules, key=itemgetter(1))
    return all(update.index(rule[0]) < update.index(rule[1]) for rule in sorted_rules)


def get_mid_page(update):
    middle_num = int(update[math.floor(len(update)/2)])
    logger.info(
        f"Middle of {update} at index {math.floor(len(update)/2)}/{len(update)} is {middle_num}")
    return middle_num

def fix_update(update, rules):
    update_rules = []
    # update_copy = update.copy()
    fixed_update = []
    for rule in rules:
        if set([rule[0], rule[1]]).issubset(update):
            update_rules.append(rule)
    
    # sorted_rules = sorted(update_rules, key=itemgetter(0,1), reverse=True)
    # semi_fixed_update = set([set([i[0], i[1]]) for i in sorted_rules])
    logger.info(f"update {update}")
    # logger.info(f"update SEMI {[int(i[0], int(i[1])) for i in sorted_rules]}")
    
    for rule in update_rules:
        if not update.index(rule[0]) < update.index(rule[1]):
            logger.info(f"update NOT Follow Rule {rule}")
            tmp = update[update.index(rule[0])]
            tmp_i = update.index(rule[0])
            tmp_i_2 = update.index(rule[1])
            update[tmp_i] = update[update.index(rule[1])]
            update[tmp_i_2] = tmp
    
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
            middle_num = get_mid_page(fixed_update)
            total_sum += middle_num

    logger.info(
        f"Total Valid Updates: {len(valid_updates)}, Summed middle pages: {total_sum}")


if __name__ == "__main__":
    main()
