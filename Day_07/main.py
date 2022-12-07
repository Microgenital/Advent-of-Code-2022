with open("input.test", "r") as f:
    data = f.read().splitlines()



def main_01(data):
    # data input is linux commands
    # go ttrough each command and execute it
    # return the value of the register a

    instructions = []
    for line in data:
        instructions.append(line.split(" "))

    for i in instructions:
        if i[0] == "$":
            print(i[1])

    """path = []
    for line in data:
        if "$" in line: # line is entered by user
            if "cd" in line and ".." in line:
                pass
            elif "cd" in line:
                pass
            elif "ls" in line:
                pass"""



def main_02(data):
    pass

if __name__ == "__main__":
    main_01(data)
    main_02(data)