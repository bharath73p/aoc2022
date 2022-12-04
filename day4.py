def parse_input(file_name):
    pair_sections = []
    with open(file_name, "r") as f:
        for line in f:
            l = line.strip()
            if len(l):
                w = l.split(",")
                e1 = list(map(int, w[0].split("-")))
                e2 = list(map(int, w[1].split("-")))
                ranges = [range(e1[0], e1[1]+1), range(e2[0], e2[1]+1)]
                pair_sections.append(ranges)
    return pair_sections

def is_fully_contained(pair):
    return 1*(set(pair[0]).issubset(pair[1]) or set(pair[1]).issubset(pair[0]))

def is_overlapping(pair):
    return 1*(len(set(pair[0]).intersection(set(pair[1]))) > 0)

def main():
    print("AoC 2022: Day 4")
    pair_sections = parse_input("input4.txt")
    fully_contained = map(is_fully_contained, pair_sections)
    print("Part 1: Sum of priorities of common items = " + str(sum(fully_contained)))
    overlapping = map(is_overlapping, pair_sections)
    print("Part 2: Sum of priorities of badges = " + str(sum(overlapping)))

if __name__=="__main__":
    main()
