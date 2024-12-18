import sys
from pathlib import Path

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from day1.logger import logger
from day1.part1 import get_file_path_from_user
from part1 import load_data_from_file

def is_report_sorted_up_to_1_fault(report: list[int]):
    fault_count = 0
    sorted_enough = True
    for level in range(len(report)-1):
        if sorted_enough and report[level] < report[level+1] and fault_count <= 1:
            continue
        else:
            fault_count += 1
            logger.info(f"#{level} Report {report} is not sorted enough, {fault_count}")
            break
    return sorted_enough

def is_report_safe_enough(report: list[int]):
	fault_count = 0
	report_safe = True
	for level in range(len(report)-1):
		if not report_safe and fault_count > 1:
			logger.info(f"#{level} Report {report} is NOT Safe, {abs(report[level] - report[level+1])}")
			break
		else:
			fault_count += 1
			report_safe = 0 < abs(report[level] - report[level+1]) <= 3
    
	return report_safe

def main():
    file_path = get_file_path_from_user()
    reports = load_data_from_file(file_path, ' ')

    safe_report_count = 0
    for report in reports:
        if is_report_sorted_up_to_1_fault(report):
            if is_report_safe_enough(report):
                safe_report_count += 1
        else:
            logger.info(f"#{reports.index(report)} Report {report} is not sorted enough, {safe_report_count}")

    logger.info(f"Safe Reports: {safe_report_count}")


if __name__ == "__main__":
    main()