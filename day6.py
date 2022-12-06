def parse_input(file_name):
    with open(file_name, "r") as f:
        for line in f:
            l = line.strip()
    return l

def scan_marker(buffer, size=4):
    for k in range(size-1, len(buffer)):
        fourchars = buffer[k-size+1:k+1]
        if len(set(fourchars)) == size:
            return fourchars, k+1
    return None, None

def main():
    print("AoC 2022: Day 6")
    buffer = parse_input("input6.txt")
    uniq, index = scan_marker(buffer)
    print("Part 1: Start of packet marker at " + str(index))
    uniq, index = scan_marker(buffer, 14)
    print("Part 2: Start of packet marker at " + str(index))

if __name__=="__main__":
    main()
