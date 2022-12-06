def parse_input(file_name):
    stacks = {}
    instructs = []
    with open(file_name, "r") as f:
        for line in f:
            l = line.rstrip()
            if len(l):
                if l.startswith("move"):
                    w = l.split()
                    instructs.append({"moves": int(w[1]), "from": int(w[3]), "to": int(w[5])})
                else:
                    i = 0
                    while i<len(l):
                        if l[i] == "[":
                            stack_num = i // 4 + 1
                            if stack_num not in stacks:
                                stacks[stack_num] = []
                            stacks[stack_num].insert(0, l[i+1])
                            i = i + 4
                        else:
                            i = i + 1
    return stacks, instructs

def perform_instr(stacks, instr):
    for _ in range(instr["moves"]):
        item = stacks[instr["from"]].pop()
        stacks[instr["to"]].append(item)
    return stacks

def perform_instr9001(stacks, instr):
    items = []
    for _ in range(instr["moves"]):
        items.append(stacks[instr["from"]].pop())
    items.reverse()
    stacks[instr["to"]].extend(items)
    return stacks

def get_stack_tops(stacks):
    tops = []
    for k in range(len(stacks.keys())):
        tops.append(stacks[k+1][-1])
    return "".join(tops)

def main():
    print("AoC 2022: Day 5")
    stacks, instructs = parse_input("input5.txt")
    for instr in instructs:
        stacks = perform_instr(stacks, instr)
    stack_tops = get_stack_tops(stacks)
    print("Part 1: Tops of stacks = " + stack_tops)
    stacks, instructs = parse_input("input5.txt")
    for instr in instructs:
        stacks = perform_instr9001(stacks, instr)
    stack_tops = get_stack_tops(stacks)
    print("Part 2: Tops of stacks with CrateMover9001 = " + stack_tops)

if __name__=="__main__":
    main()
