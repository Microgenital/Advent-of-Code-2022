with open("input.test") as f:
    data = f.read().splitlines()


def main_01(data):
    # sort instructions and creates
    creates = []
    instructions = []
    for line in data:
        if "move" in line:
            instructions.append(line)
        else:
            creates.append(line)

    # print as 2d array
    for i in range(len(creates)):
        print(creates[i])


def main_02(data):
    pass


if __name__ == "__main__":
    print(main_01(data))
    print(main_02(data))
