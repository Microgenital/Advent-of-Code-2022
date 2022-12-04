with open("input.prod") as f:
    data = f.read().splitlines()


def main_01(data):
    data2 = []
    for line in data:
        data2.append(line.split(","))

    count = 0
    for i in data2:
        nums_1 = []
        nums_2 = []
        list_1 = []
        list_2 = []

        for j in i[0].split("-"):
            nums_1.append(int(j))

        for j in i[1].split("-"):
            nums_2.append(int(j))

        for i in range(nums_1[0], nums_1[1] + 1):
            list_1.append(i)
        for i in range(nums_2[0], nums_2[1] + 1):
            list_2.append(i)

        if set(list_1).issubset(set(list_2)) or set(list_2).issubset(set(list_1)):
            count += 1

    print(f"Solution 01: {count}")


def main_02(data):
    data2 = []
    for line in data:
        data2.append(line.split(","))

    count = 0
    for i in data2:
        nums_1 = []
        nums_2 = []
        list_1 = []
        list_2 = []

        for j in i[0].split("-"):
            nums_1.append(int(j))

        for j in i[1].split("-"):
            nums_2.append(int(j))

        for i in range(nums_1[0], nums_1[1] + 1):
            list_1.append(i)
        for i in range(nums_2[0], nums_2[1] + 1):
            list_2.append(i)

        if len(list_1) >= len(list_2):
            for i in list_1:
                if i in list_2:
                    count += 1
                    break
        else:
            for i in list_2:
                if i in list_1:
                    count += 1
                    break

    print(f"Solution 02: {count}")



if __name__ == "__main__":
    main_01(data)
    main_02(data)
