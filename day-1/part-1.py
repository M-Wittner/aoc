import sys
from logger import logger

def load_data_from_file(path: str):
	with open('in.txt', 'r') as input_file:
		left_nums = []
		right_nums = []
		for line in input_file:
			left, right = line.strip().rsplit('   ')
			left_nums.append(int(left))
			right_nums.append(int(right))
		
	return left_nums, right_nums


def calc_diff(left: list[int] , right: list[int]):
	line_count = 0
	total_distance = 0
	for i in range(len(left)):
		distance = abs(left[i] - right[i])
		logger.info(f"Distance between {left[i]} and {right[i]} is: {distance}")
		
		total_distance += distance
		line_count += 1
		logger.info(f"#{line_count} Line distance: {distance}")
		logger.info(f"#{line_count} Total distance: {total_distance}")

	print(f"#{line_count} Total distance: {total_distance}")
	return total_distance


def get_file_path_from_user():
	if len(sys.argv) != 2:
		logger.error(f"Too many argument({len(sys.argv)}), expecting 1")
		exit(1)
	
	return sys.argv[1]


def main():
	file_path = get_file_path_from_user()
	left_nums, right_nums = load_data_from_file(file_path)
	right_sorted = sorted(right_nums)
	left_sorted = sorted(left_nums)
	calc_diff(left_sorted, right_sorted)


if __name__ == "__main__":
		main()
