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

    priority_total = 0
    total_lines = 0
    total_maches = 0
    for rucksack_inventory in input:
        rucksack_inventory = rucksack_inventory.strip()
        halfway_point = int(len(rucksack_inventory)/2)
        first_compartment = rucksack_inventory[:halfway_point]
        second_compartment = rucksack_inventory[halfway_point:]

        for item in first_compartment:
            if item in second_compartment:
                total_maches += 1
                common_priority = letter_set.index(item) + 1
                priority_total += common_priority
                break

        total_lines += 1

    print(f"Total lines: {total_lines}")
    print(f"Total matches: {total_maches}")
    print(f"Priority total is {priority_total}.")

if __name__ == "__main__":
    main()