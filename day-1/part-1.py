

def main():
	total_distance = 0
	open('out.txt', 'w').close()
	with open('in.txt', 'r') as input_file, \
		 open('out.txt', 'w') as out_file:
		line_count = 0

		left_nums = []
		right_nums = []
		for line in input_file:
			left, right = line.strip().rsplit('   ')
			left_nums.append(int(left))
			right_nums.append(int(right))
		right_sorted = sorted(right_nums)
		left_sorted = sorted(left_nums)

		for i in range(len(right_sorted)):
			distance = abs(right_sorted[i] - left_sorted[i])
			out_file.write(f"Distance between {right_sorted[i]} and {left_sorted[i]} is: {distance}\n")
			total_distance += distance
			
			line_count += 1
			out_file.write(f"#{line_count} Line distance: {distance}"+"\n")
			out_file.write(f"#{line_count} Total distance: {total_distance}"+"\n")
			print(f"#{line_count} Line distance: {distance}")
		print(f"#{line_count} Total distance: {total_distance}")
	
if __name__ == "__main__":
		main()