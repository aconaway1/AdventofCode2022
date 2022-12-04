import string

def get_letter_set():
    lower_letter_set = set(string.ascii_lowercase)
    upper_letter_set = set(string.ascii_uppercase)
    lower_letter_set = sorted(lower_letter_set)
    upper_letter_set = sorted(upper_letter_set)
    letter_set = lower_letter_set + upper_letter_set
    return letter_set

def main():
    rucksack_input_file = "rucksack_input.txt"

    with open(rucksack_input_file, 'r') as file:
        input = file.readlines()

    letter_set = get_letter_set()

    read_index = 0
    total_priority = 0
    group_items = []
    group_priority = 0
    group_count = 1
    for line in input:
        print(f"Processing line {line}")
        line = line.strip()
        if read_index > 2:
            print("Group complete")
            # print(f"GROUP ITEMS: {group_items}")
            first_rucksack_set = set(group_items[0])
            second_rucksack_set = set(group_items[1])
            third_rucksack_set = set(group_items[2])
            intersect = first_rucksack_set.intersection(second_rucksack_set).intersection(third_rucksack_set)
            group_priority = letter_set.index(list(intersect)[0]) + 1
            total_priority += group_priority

            print(f"Group {group_count} matches {intersect} with a priority of {group_priority}.")

            group_count += 1
            read_index = 1
            group_items = []
            group_items.append(line)
            pass

        else:
            group_items.append(line)
            read_index += 1

    first_rucksack_set = set(group_items[0])
    second_rucksack_set = set(group_items[1])
    third_rucksack_set = set(group_items[2])
    intersect = first_rucksack_set.intersection(second_rucksack_set).intersection(third_rucksack_set)
    group_priority = letter_set.index(list(intersect)[0]) + 1
    total_priority += group_priority
    print(f"Group {group_count} matches {intersect} with a priority of {group_priority}.")

    print(group_count, total_priority)


if __name__ == "__main__":
    main()