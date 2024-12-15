from logger import logger
import importlib
part1 = importlib.import_module("part-1")

def get_num_of_occurrences(num: int, list: list[int]):
	return list.count(num)

def calc_similarity_score(num: int, times: int):
	return num * times

def main():
	file_path = part1.get_file_path_from_user()
	left_nums, right_nums = part1.load_data_from_file(file_path)
	similarity_score = 0
	reducted_right_nums = right_nums
	for num in left_nums:
		occur = get_num_of_occurrences(num, reducted_right_nums)
		reducted_right_nums = list(filter(lambda x: x != num, reducted_right_nums))
		similarity_score += calc_similarity_score(num, occur)

	logger.info(f"Similarity Score: {similarity_score}")

	
if __name__ == "__main__":
	main()

