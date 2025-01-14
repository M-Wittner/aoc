import sys
from pathlib import Path
# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from day1.part1 import get_file_path_from_user
from day1.logger import logger
import re, math
from operator import itemgetter



def load_data_from_file(file_path):
    with open(file_path, 'r') as input_file:
        rule_pattern = re.compile('^(\d+\|\d+)')
        update_pattern = re.compile('^\d+(,\d+)*$')
        rules = []
        updates = []
        for line_raw in input_file:
            line = line_raw.strip()
            if rule_pattern.match(line):
                rule = tuple(line.split('|'))
                rules.append(rule)
            if update_pattern.match(line):
                updates.append(line.split(','))

    return rules, updates


def is_update_valid(update, rules):
    for rule in rules:
        if set(rule).issubset(update):
            logger.info(f"Rule {rule} is in update {update}")
            if not update[update.index(rule[0])] < update[update.index(rule[1])]:
                return False
    return True


def main():
    file_path = get_file_path_from_user()
    rules, updates = load_data_from_file(file_path)
    valid_updates= []
    total_sum = 0

    for update in updates:
        # print(update)
        update_rules = []
        for rule in rules:
            if set(rule).issubset(update):
                logger.info(f"Rule {rule} is in update {update}")
                if update.index(rule[0]) < update.index(rule[1]):
                    # logger.info(f"Update {update} > {update[update.index(rule[0])], update.index(rule[0])}|{update[update.index(rule[1])], update.index(rule[1])} is matching rule {rule}")
                    update_rules.append(rule)
            else:
                logger.info(f"Rule {rule} is not in update")
                

        sorted_rules = sorted(update_rules, key=itemgetter(0, 1), reverse=True)
        logger.info(f"Update Rules {update_rules}")
        logger.info(f"Sorted Rules {sorted_rules}")
        logger.info(f"Update {update}")
        
        is_update_valid = all(update.index(rule[0]) < update.index(rule[1]) for rule in update_rules)
        if is_update_valid:
            valid_updates.append(update)
            logger.info(f"Update is Valid!")
            middle_num = int(update[math.floor(len(update)/2)])
            logger.info(f"Middle of update is {middle_num}")
            total_sum += middle_num
            
        
    logger.info(f"Total Valid Updates: {len(valid_updates)}, Summed middle pages: {total_sum}")


if __name__ == "__main__":
    main()
