with open("input.prod", "r") as f:
    data = f.read()


def main_01(data):
    datapoints = []
    index = 0

    # write always the next 4 datapoints to the list
    # check if they have duplicates
    # if they have duplicates, write the next 4 datapoints to the list and check again
    for i in range(0, len(data)):
        for b in range(4):
            datapoints.append(data[index])
            index += 1
        # print(datapoints)
        if len(datapoints) == len(set(datapoints)):
            # print("False, keine Duplicates", i + 4)
            break
        else:
            # print("True, Duplicates")
            pass

        datapoints = []
        index -= 3

    print(f"Solution Part 1: {i + 4}")


def main_02(data):
    datapoints = []
    index = 0

    # same as 1, but with 14 datapoints
    for i in range(0, len(data)):
        for b in range(14):
            datapoints.append(data[index])
            index += 1
        # print(datapoints)
        if len(datapoints) == len(set(datapoints)):
            # print("False, keine Duplicates", i + 4)
            break
        else:
            # print("True, Duplicates")
            pass

        datapoints = []
        index -= 13

    print(f"Solution Part 1: {i + 14}")


if __name__ == "__main__":
    main_01(data)
    main_02(data)
