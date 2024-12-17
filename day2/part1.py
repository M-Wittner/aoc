import sys
from pathlib import Path

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from day1.logger import logger
from day1.part1 import get_file_path_from_user

def load_data_from_file(path: str, delimiter = '   '):
	with open(path, 'r') as input_file:
		lines = []
		for line in input_file:
			str_line = line.strip().rsplit(delimiter)
			lines.append(list(map(int, str_line)))
	return lines

def is_report_sorted(report: list[int]):
    return (all(report[i] < report[i + 1] for i in range(len(report) - 1))) or (all(report[i] > report[i + 1] for i in range(len(report) - 1)))
				  
def is_report_safe(report: list[int]):
	report_safe = True
	for level in range(len(report)-1):
		if not report_safe:
			break
		else:
			report_safe = 0 < abs(report[level] - report[level+1]) <= 3
			logger.info(f"#{level} Report {report} is Safe {report_safe}, {abs(report[level] - report[level+1])}")
	
	return report_safe
		

def main():
    file_path = get_file_path_from_user()
    reports = load_data_from_file(file_path, ' ')

    safe_report_count = 0
    for report in reports:
        if is_report_sorted(report):
            if is_report_safe(report):
                safe_report_count += 1

    logger.info(f"Safe Reports: {safe_report_count}")


if __name__ == "__main__":
    main()
