import sys
from pathlib import Path
from itertools import compress

# Add the project root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from day1.logger import logger
from day1.part1 import get_file_path_from_user
from part1 import load_data_from_file, return_is_report_safe


def main():
    file_path = get_file_path_from_user()
    reports = load_data_from_file(file_path, ' ')

    safe_report_count = 0
    for report in reports:
        if return_is_report_safe(report):
            safe_report_count += 1
        else:
            for i in range(len(report)):
                report_copy = report.copy()
                diced_report = report_copy[:i]+report_copy[i+1:]
                if return_is_report_safe(diced_report):
                    safe_report_count += 1
                    print(f"Safe Reports: {safe_report_count}")
                    break

    logger.info(f"Safe Reports: {safe_report_count}")

if __name__ == "__main__":
    main()