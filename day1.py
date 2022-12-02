CALORIES_FILE = "calories.txt"

def main():
    elf_calorie_totals = {}

    with open(CALORIES_FILE, 'r') as file:
        calories = file.readlines()

    elf_calories = 0
    elf_number = 1
    for calorie_line in calories:
        if calorie_line == "\n":
            elf_calorie_totals[elf_number] = elf_calories
            elf_number = elf_number + 1
            elf_calories = 0
            continue
        elf_calories = elf_calories + int(calorie_line.strip())

    elf_calorie_totals[elf_number] = elf_calories


    top_three_total_calories = 0
    for _ in range(0,3):
        max_elf_key = max(elf_calorie_totals, key=elf_calorie_totals.get)
        print(f"Elf number {max_elf_key} is carrying the most calories at {elf_calorie_totals[max_elf_key]}.")
        top_three_total_calories = top_three_total_calories + elf_calorie_totals[max_elf_key]
        elf_calorie_totals.pop(max_elf_key)
    print(f"The top 3 elves are carrying {top_three_total_calories} calories.")

if __name__ == "__main__":
    main()