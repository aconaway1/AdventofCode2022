import re
import string


def main():
    INPUT_FILE = "day5_input.txt"

    # The stacks dict is keyed on the stack number
    stacks = {
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': [],
    }

    with open(INPUT_FILE, 'r') as file:
        lines = file.read().splitlines()

    # Split the input file into the initial stack arrangement (0-8) and the instruction set (10-)
    stack_lines = lines[:8]
    move_lines = lines[10:]
    # Generate a list of valid box IDs to check against
    valid_boxes = string.ascii_uppercase
    # Go through the stack lines to populate the initial arrangement
    # We do this by keying off the column (col 1 for stack 1, 5 for 2, etc.)
    for stack_line in stack_lines:
        if len(stack_line) >= 1 and stack_line[1] in valid_boxes:
            stacks['1'].append(stack_line[1])
        if len(stack_line) >= 5 and stack_line[5] in valid_boxes:
            stacks['2'].append(stack_line[5])
        if len(stack_line) >= 9 and stack_line[9] in valid_boxes:
            stacks['3'].append(stack_line[9])
        if len(stack_line) >= 13 and stack_line[13] in valid_boxes:
            stacks['4'].append(stack_line[13])
        if len(stack_line) >= 17 and stack_line[17] in valid_boxes:
            stacks['5'].append(stack_line[17])
        if len(stack_line) >= 21 and stack_line[21] in valid_boxes:
            stacks['6'].append(stack_line[21])
        if len(stack_line) >= 25 and stack_line[25] in valid_boxes:
            stacks['7'].append(stack_line[25])
        if len(stack_line) >= 29 and stack_line[29] in valid_boxes:
            stacks['8'].append(stack_line[29])
        if len(stack_line) >= 33 and stack_line[33] in valid_boxes:
            stacks['9'].append(stack_line[33])
    popped_elements = []
    # Go through the movements
    for move_line in move_lines:
        popped_elements.clear()
        # Do a regex to pull out the number of crates to move as well as src and dst stacks
        match_move = re.match("move (\d+) from (\d+) to (\d)", move_line)
        # If there is a match...
        if match_move:
            # Set these vars based on the regex match
            number_to_move = int(match_move.group(1))
            src_stack = match_move.group(2)
            dst_stack = match_move.group(3)
            popped_elements = stacks[src_stack][:number_to_move]
            stacks[dst_stack] = popped_elements + stacks[dst_stack]
            del stacks[src_stack][:number_to_move]
        else:
            print("That line didn't look right.")
            continue

    result_string = ""
    for stack in stacks.keys():
        result_string += stacks[stack][0]
        print(f"STACK: {stacks[stack]}")

    print(F"This is it >> {result_string}")

if __name__ == "__main__":
    main()