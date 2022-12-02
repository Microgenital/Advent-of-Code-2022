with open("input.prod", "r") as f:
    lines = f.readlines()

def main_01(data):
    plays = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",

        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }

    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    score = 0
    for line in data:
        enemy_play = line[0]
        player_play = line[2]

        if plays[enemy_play] == plays[player_play]:
            score += scores[player_play]
            score += 3
        elif plays[enemy_play] == "Rock" and plays[player_play] == "Paper":
            score += scores[player_play]
            score += 6
        elif plays[enemy_play] == "Rock" and plays[player_play] == "Scissors":
            score += scores[player_play]
            score += 0
        elif plays[enemy_play] == "Paper" and plays[player_play] == "Rock":
            score += scores[player_play]
            score += 0
        elif plays[enemy_play] == "Paper" and plays[player_play] == "Scissors":
            score += scores[player_play]
            score += 6
        elif plays[enemy_play] == "Scissors" and plays[player_play] == "Rock":
            score += scores[player_play]
            score += 6
        elif plays[enemy_play] == "Scissors" and plays[player_play] == "Paper":
            score += scores[player_play]
            score += 0

    print("Score for first Answer is: ", score)


def main_02(data):
    plays = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",

        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }

    scores = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    score = 0
    for line in data:
        enemy_play = line[0]
        outcome = line[2]

        if outcome == "X": # Loose
            if plays[enemy_play] == "Rock":
                score += scores["Z"]
            elif plays[enemy_play] == "Paper":
                score += scores["X"]
            elif plays[enemy_play] == "Scissors":
                score += scores["Y"]
            score += 0

        elif outcome == "Y": # Draw
            if plays[enemy_play] == "Rock":
                score += scores["X"]
            elif plays[enemy_play] == "Paper":
                score += scores["Y"]
            elif plays[enemy_play] == "Scissors":
                score += scores["Z"]
            score += 3

        elif outcome == "Z": # Win
            if plays[enemy_play] == "Rock":
                score += scores["Y"]
            elif plays[enemy_play] == "Paper":
                score += scores["Z"]
            elif plays[enemy_play] == "Scissors":
                score += scores["X"]
            score += 6



    print("Score for second Answer is: ", score)

if __name__ == "__main__":
    # main_01(lines)
    main_02(lines)