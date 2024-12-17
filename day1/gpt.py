def calculate_total_distance(file_path):
    total_distances = []

    with open(file_path, "r") as file:
        for line_number, line in enumerate(file.readlines(), start=1):
            # Split and parse the two columns into two lists of integers
            columns = line.split()
            if len(columns) != 2:
                continue  # Skip invalid lines

            left = list(map(int, columns[0].split(',')))
            right = list(map(int, columns[1].split(',')))
            # Sort both lists
            left.sort()
            right.sort()

            print(left)
            # Compute the total distance
            total_distance = sum(abs(l - r) for l, r in zip(left, right))
            total_distances.append((line_number, total_distance))

    return total_distances

# Path to the input file
file_path = "in.txt"  # Replace with the actual file path if different

# Calculate and print the results
def main():
    distances = calculate_total_distance(file_path)
    for line_number, total_distance in distances:
        print(f"# Line {line_number} Total distance: {total_distance}")

if __name__ == "__main__":
    main()
