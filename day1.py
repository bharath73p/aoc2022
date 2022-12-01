import re

def parse_input(file_name):
    elves = []
    elf = []
    with open(file_name, "r") as f:
        for line in f:
            l = line.strip()
            if len(l):
                elf.append(int(l))
            else:
                elves.append(elf)
                elf = []
    return elves

def total_elf_calories(elves):
    totals = []
    for elf in elves:
        totals.append(sum(elf))
    return totals

def main():
    print("AoC 2022: Day 1")
    elves = parse_input("input1.txt")
    total_cals = total_elf_calories(elves)
    print("Part 1: Most calories carried by an elf = " + str(max(total_cals)))
    stotal_cals = sorted(total_cals, reverse=True)
    print("Part 2: Sum of calories for top 3 elves = " + str(stotal_cals[0] + stotal_cals[1] + stotal_cals[2]))

if __name__=="__main__":
    main()
