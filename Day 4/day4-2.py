def get_range(dashed_numbers):
    returned_list = []
    first, last = dashed_numbers.split('-')
    first = int(first)
    last = int(last)
    for i in range(first, last + 1):
        returned_list.append(i)

    return returned_list

def main():
    INPUT_FILE = "day4_input.txt"

    subset_count = 0
    with open(INPUT_FILE, 'r') as file:
        lines = file.read().splitlines()

    for line in lines:
        first, second = line.split(",")
        first_set = set(get_range(first))
        second_set = set(get_range(second))

        intersected_set = first_set.intersection(second_set)
        if len(intersected_set) > 0:
            subset_count += 1

    print(f"Found {subset_count} matches.")

if __name__ == "__main__":
    main()