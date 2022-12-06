def is_unique_set(characters):
    compare_set = set(characters)

    if len(compare_set) == 14:
        return True
    return False

def main():
    INPUT_FILE = "day6_input.txt"

    with open(INPUT_FILE, 'r') as file:
        datastream = file.readline().strip()

    last_fourteen = ""
    start_tracker = 0
    for character in datastream:
        start_tracker += 1
        last_fourteen += character
        if len(last_fourteen) < 14:
            continue
        if is_unique_set(last_fourteen):
            print(f"The first unique four-character set is {last_fourteen} starting at {start_tracker}.")
            break
        last_fourteen = last_fourteen[1:]


if __name__ == "__main__":
    main()