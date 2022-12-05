def score_it(opponent, me):
    if opponent == "A":
        if me == "X":
            return 4
        if me == "Y":
            return 8
        if me == "Z":
            return 3
    if opponent == "B":
        if me == "X":
            return 1
        if me == "Y":
            return 5
        if me == "Z":
            return 9
    if opponent == "C":
        if me == "X":
            return 7
        if me == "Y":
            return 2
        if me == "Z":
            return 6

def main():
    winning_score = 6
    draw_score = 3
    lose_score = 0

    rock_score = 1
    paper_score = 2
    scissors_score = 3

    total_score = 0

    with open("rps.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        myplay, oppplay = line.split()
        score = score_it(myplay, oppplay)
        total_score = total_score + score

    print(f"Total score is {total_score}.")



if __name__ == "__main__":
    main()