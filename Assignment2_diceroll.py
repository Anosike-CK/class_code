import random
import time
User1 = input('Please enter your username : ')
User2 = input ('Please enter your username : ')
User1points = 0
User2points = 0
player1Tiebreaker = 0
player2Tiebreaker = 0

i = 0
while i <= 1:

    game_starter =  input('Player 1, type your name? ')
    print(f'It is your turn {game_starter}')
    if game_starter == User1:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dietotal = die1 + die2
        print(dietotal)
        User1points += 10 if dietotal % 2 == 0 else -5       
        print(User1points)
        if die1 == die2:
            print(f'your first and second dies have same number {die1}')
            die3 = random.randint(1,6)
            User1points += die3
        time.sleep(1)
    print(f'{game_starter} just played, it is your turn player 2')
    User2_input = input('Player 2, please enter your name to roll : ')
    if User2_input == User2:

        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dietotal = die1 + die2
        print(dietotal)
        User2points += 10 if dietotal % 2 == 0 else -5   
        print(User2points)

        if die1 == die2:

            die3 = random.randint(1,6)
            User1points += die3
    i += 1


if User1points == User2points:
    while player1Tiebreaker == player2Tiebreaker:
        player1Tiebreaker = random.randint(1,6)
        player2Tiebreaker = random.randint(1,6)

        if player1Tiebreaker > player2Tiebreaker:
            player2Points = 0
        elif player2Tiebreaker > player1Tiebreaker:
            player1Points = 0
print(User1points,User2points)
if User1points > User2points:
    print(f'{User1} has {User1points} and {User2} has {User2points} therefore {User1} is the winner')
else:
    print(f'{User2} has {User2points} and {User1} has {User1points} therefore {User2} is the winner')

