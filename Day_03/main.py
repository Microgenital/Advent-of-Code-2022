with open("input.prod", "r") as f:
    lines = f.readlines()


def main_01(data):
    score = 0
    priority = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52,
    }

    rucksack = []
    for line in data:
        line1 = line[0:int((len(line) - 1) / 2)]
        line2 = line[int((len(line) - 1) / 2):len(line) - 1]
        rucksack.append([line1, line2])

        # find the letter that appears in both lines
        for letter in line1:
            if letter in line2:
                # print(letter)
                score += priority[letter]
                break

    print("Part 01: ", score)


def main_02(data):
    data_index = 0
    # remove \n from the end of the line
    for line in data:
        data[data_index] = line[0:len(line) - 1]
        data_index += 1

    priority = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52,
    }

    score = 0
    group_index = 0
    for i in range(int(len(data) / 3)):
        line1 = data[group_index]
        line2 = data[group_index + 1]
        line3 = data[group_index + 2]
        for char in priority:
            if char in line1:
                if char in line2:
                    if char in line3:
                        # print(char)
                        group_index += 3
                        score += priority[char]

    print("Part 02: ", score)


if __name__ == "__main__":
    main_01(lines)
    main_02(lines)
