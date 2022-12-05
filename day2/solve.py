point_values = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

file_input = open('./day2/input.txt').readlines()
print(f"Input Size: {len(file_input)}")

#Part 1
score = 0
for game in file_input:
    letters = game.split(' ')
    my_letter = letters[1].strip()
    opponent_letter = letters[0].strip()
    score += point_values[my_letter]
    if(my_letter == 'X' and opponent_letter == 'C'):
        score += 6
        print('win')
    elif(my_letter == 'Y' and opponent_letter == 'A'):
        score += 6
        print('win')
    elif(my_letter == 'Z' and opponent_letter == 'B'):
        score += 6
        print('win')
    elif(point_values[my_letter] == point_values[opponent_letter]):
        score += 3
        print('tie')
print(f"Part 1 : {score}")

#Part 2
losing_map = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}
winning_map = {
    'C': 'A',
    'A': 'B',
    'B': 'C',
}
score = 0
for game in file_input:
    letters = game.split(' ')
    opponent_letter = letters[0].strip()
    game_goal = letters[1].strip()
    #X, Y, Z = lose, draw, win
    if(game_goal == 'X'):
        #we need to lose
        our_letter = losing_map[opponent_letter]
        score += point_values[our_letter]
    elif (game_goal == 'Y'):
        #we need to draw
        score += point_values[opponent_letter]
        score += 3
    elif (game_goal == 'Z'):
        #we need to win
        our_letter = winning_map[opponent_letter]
        score += point_values[our_letter]
        score += 6
print(f"Part 2 : {score}")