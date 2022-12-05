with open("input.prod") as f:
    data = f.read().splitlines()


def main_01(data):
    # sort instructions and creates
    creates = []
    instructions = []

    # sort input in creates and instructions
    for line in data:
        if "move" in line:
            instructions.append(line)
        else:
            continue

    creates_test = [
        [],
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ]

    """
    Had to manually enter the creates_list, because I couldn't figure out how to sort it automatically.
    """
    creates = [
        [],
        ["V", "C", "D", "R", "Z", "G", "B", "W"],
        ["G", "W", "F", "C", "B", "W", "T", "V"],
        ["C", "B", "S", "N", "W"],
        ["Q", "G", "M", "N", "J", "V", "C", "P"],
        ["T", "S", "L", "F", "D", "H", "B"],
        ["J", "V", "T", "W", "M", "N"],
        ["P", "F", "L", "C", "S", "T", "G"],
        ["B", "D", "Z"],
        ["M", "N", "Z", "W"]
    ]

    # make list for all instructions readable
    lines_clr = []
    for i in instructions:
        lines_clr.append(i.split(" "))

    # execute instructions
    for i in lines_clr:
        count = i[1]
        from_ = i[3]
        to_ = i[5]
        for c in range(int(count)):
            creates[int(to_)].append(creates[int(from_)].pop())

    # create and print solution
    solution = ""
    for i in creates:
        if len(i) == 0:
            continue
        solution += i[-1]
    print(f"Solution Part 1: {solution}")


def main_02(data):
    # sort instructions and creates
    creates = []
    instructions = []

    # sort input in creates and instructions
    for line in data:
        if "move" in line:
            instructions.append(line)
        else:
            continue

    creates_test = [
        [],
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ]

    """
    Had to manually enter the creates_list, because I couldn't figure out how to sort it automatically.
    """
    creates = [
        [],
        ["V", "C", "D", "R", "Z", "G", "B", "W"],
        ["G", "W", "F", "C", "B", "W", "T", "V"],
        ["C", "B", "S", "N", "W"],
        ["Q", "G", "M", "N", "J", "V", "C", "P"],
        ["T", "S", "L", "F", "D", "H", "B"],
        ["J", "V", "T", "W", "M", "N"],
        ["P", "F", "L", "C", "S", "T", "G"],
        ["B", "D", "Z"],
        ["M", "N", "Z", "W"]
    ]

    # make list for all instructions readable
    lines_clr = []
    for i in instructions:
        lines_clr.append(i.split(" "))

    # execute instructions
    for i in lines_clr:
        amount = int(i[1])
        from_ = int(i[3])
        to_ = int(i[5])
        for c in range(amount):
            creates[to_].append(creates[from_][-amount])
            creates[from_].pop(-amount)
            amount -= 1

    # solution for test input is: MCD

    # create and print solution
    solution = ""
    for i in creates:
        if len(i) == 0:
            continue
        solution += i[-1]
    print(f"Solution Part 2: {solution}")


if __name__ == "__main__":
    main_01(data)
    main_02(data)
