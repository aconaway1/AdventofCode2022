def is_unique_set(characters):
    compare_set = set(characters)

    if len(compare_set) == 4:
        return True
    return False

def main():
    INPUT_FILE = "day6_input.txt"

    with open(INPUT_FILE, 'r') as file:
        datastream = file.readline().strip()

    last_four = ""
    start_tracker = 0
    for character in datastream:
        start_tracker += 1
        last_four += character
        if len(last_four) < 4:
            continue
        if is_unique_set(last_four):
            print(f"The first unique four-character set is {last_four} starting at {start_tracker}.")
            break
        last_four = last_four[1:]


if __name__ == "__main__":
    main()