with open("input.test") as f:
    data = f.read().splitlines()

def main_01(data):
    data2 = []
    for line in data:
        data2.append(line.split(","))


    for i in data2:
        first_num = int(i[0][0])
        second_num = int(i[0][2])
        for num in range(first_num, second_num + 1):
            print(num)
        print("\n")



def main_02(data):
    pass

if __name__ == "__main__":
    main_01(data)
    main_02(data)