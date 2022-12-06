with open("input.prod", "r") as f:
    data = f.read()

def main_01(data):
    datapoints = []
    index = 0
    for i in range(0, len(data)):
        for b in range(4):
            datapoints.append(data[index])
            index += 1
        print(datapoints)
        if len(datapoints) == len(set(datapoints)):
            print("False, keine Duplicates", i + 4)
            break
        else:
            print("True, Duplicates")

        datapoints = []
        index -= 3

        print(i + 4)


"""
mjqjpqmgbljsphdztnvjfqwrcgsmlb
       ^
       
"""
def main_02(data):
    pass

if __name__ == "__main__":
    main_01(data)
    main_02(data)
