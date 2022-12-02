def score_it(opponent, outcome):
    winning_score = 6
    draw_score = 3
    lose_score = 0
    rock_score = 1
    paper_score = 2
    scissors_score = 3
    if opponent == "A":
        if outcome == "X":
            return lose_score + scissors_score
        if outcome == "Y":
            return draw_score + rock_score
        if outcome == "Z":
            return winning_score + paper_score
    if opponent == "B":
        if outcome == "X":
            return lose_score + rock_score
        if outcome == "Y":
            return draw_score + paper_score
        if outcome == "Z":
            return winning_score + scissors_score
    if opponent == "C":
        if outcome == "X":
            return lose_score + paper_score
        if outcome == "Y":
            return draw_score + scissors_score
        if outcome == "Z":
            return winning_score + rock_score

def main():


    total_score = 0

    with open("rps.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        print(f"LINE>>>{line}<<<")
        myplay, outcome = line.split()
        score = score_it(myplay, outcome)
        print(score)
        total_score = total_score + score

    print(f"Total score is {total_score}.")



if __name__ == "__main__":
    main()