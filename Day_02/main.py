with open("input.prod", "r") as f:
    lines = f.readlines()

# for line in lines:
    # print(line)

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
for line in lines:
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
