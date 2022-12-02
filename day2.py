def parse_input(file_name):
    rounds = []
    with open(file_name, "r") as f:
        for line in f:
            l = line.strip()
            if len(l):
                w = l.split()
                rounds.append((w[0], w[1]))
    return rounds

def get_score(shape, outcome):
    shape_points = {"r": 1, "p": 2, "s": 3}
    outcome_points = {"l": 0, "d": 3, "w": 6}
    return shape_points[shape] + outcome_points[outcome]

def get_outcome(they, you):
    who_beats_who = {"r": "s", "p": "r", "s": "p"}
    if you == they:
        return "d"
    elif who_beats_who[you] == they:
        return "w"
    else:
        return "l"

def score_rounds(rounds):
    scores = []
    for r in rounds:
        scores.append(get_score(r[1], get_outcome(*r)))
    return scores

def translate1(rounds):
    translation = {"A": "r", "B": "p", "C": "s", "X": "r", "Y": "p", "Z": "s"}
    rrounds = []
    for r in rounds:
        rrounds.append((translation[r[0]], translation[r[1]]))
    return rrounds

def translate2(rounds):
    translation = {"A": "r", "B": "p", "C": "s", "X": "l", "Y": "d", "Z": "w"}
    who_beats_who = {"r": "s", "p": "r", "s": "p"}
    who_loses_who = {"s": "r", "r": "p", "p": "s"}
    rrounds = []
    for r in rounds:
        they = translation[r[0]]
        outcome = translation[r[1]]
        if outcome == "d":
            rrounds.append((they, they))
        elif outcome == "l":
            rrounds.append((they, who_beats_who[they]))
        else:
            rrounds.append((they, who_loses_who[they]))
    return rrounds

def main():
    print("AoC 2022: Day 2")
    rounds = parse_input("input2.txt")
    rounds1 = translate1(rounds)
    scores = score_rounds(rounds1)
    print("Part 1: Total score by strategy guide = " + str(sum(scores)))
    rounds2 = translate2(rounds)
    scores = score_rounds(rounds2)
    print("Part 2: Total score by strategy guide = " + str(sum(scores)))

if __name__=="__main__":
    main()
