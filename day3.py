def parse_input(file_name):
    rucksacks = []
    with open(file_name, "r") as f:
        for line in f:
            l = line.strip()
            llen = len(l)
            if llen:
                hallen = llen//2
                rucksacks.append((l[:hallen], l[hallen:]))
    return rucksacks

def get_common_item(t_bags):
    s_bags = (set(bag) for bag in t_bags)
    return list(set.intersection(*s_bags))[0]

def get_priority(item):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(item) + 1

def groupise(rucksacks):
    groups = []
    rlen = len(rucksacks)
    for k in range(rlen//3):
        group = []
        for i in range(3):
            bag = rucksacks[3*k+i]
            group.append(bag[0]+bag[1])
        groups.append(group)
    return groups

def main():
    print("AoC 2022: Day 3")
    rucksacks = parse_input("input3.txt")
    common_items = map(get_common_item, rucksacks)
    priorities = map(get_priority, common_items)
    print("Part 1: Sum of priorities of common items = " + str(sum(priorities)))
    groups = groupise(rucksacks)
    badges = map(get_common_item, groups)
    priorities = map(get_priority, badges)
    print("Part 2: Sum of priorities of badges = " + str(sum(priorities)))

if __name__=="__main__":
    main()
