with open("input.prod") as f:
    data = f.read().splitlines()
    f.close()


def main():
    lists = []
    output = []
    sums = []
    summ = 0

    # sort the data for each elf in a different list
    for i in data:
        if i == "":
            lists.append(output)
            output = []
        else:
            output.append(i)
    lists.append(output)

    # for each elf, count the calories
    for i in lists:
        for j in i:
            summ += int(j)
        sums.append(summ)
        summ = 0

    # highest amout of calorie
    print(f"Solution 01: {max(sums)}")

    # sort the list sums descending
    sums.sort(reverse=True)
    print(f"Solution 02: {sums[0] + sums[1] + sums[2]}")


if __name__ == "__main__":
    main()
