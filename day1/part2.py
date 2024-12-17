from logger import logger
from part1 import get_file_path_from_user, load_data_from_file

def get_num_of_occurrences(num: int, list: list[int]):
	return list.count(num)

def calc_similarity_score(num: int, times: int):
	return num * times

def main():
	file_path = get_file_path_from_user()
	left_nums, right_nums = load_data_from_file(file_path)
	similarity_score = 0
	for num in left_nums:
		occur = get_num_of_occurrences(num, right_nums)
		self_occur = get_num_of_occurrences(num, left_nums)
		right_nums = list(filter(lambda x: x != num, right_nums))
		left_nums = list(filter(lambda x: x != num, left_nums))
		similarity_score += calc_similarity_score(num, occur*self_occur)

	logger.info(f"Similarity Score: {similarity_score}")

	
if __name__ == "__main__":
	main()

