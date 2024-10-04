# importing random module
import random 

# make a list of rock, paper, and scissors
lst = ['rock', 'scissors', 'paper']

print('===== WELCOME TO THE ROCK, PAPER AND SCISSORS GAME =====')
# asking for number of stage
n = int(input('input stage: '))

# make a condition for player
def rules(player1, player2):
    # initiate 2 variable for score player 1 and score player 2
    score1 = 0
    score2 = 0
    # if the player 1 choose the same player 2
    # then the score will increase zero
    if (player1 == player2):
        score1 += 0
        score2 += 0
    # if the player choose rock and other choose scissors
    # then the rock win
    if (player_1 == 'rock') and (comp == 'scissors'):
        score1 += 1
    # if the player choose paper and other choose rock
    # then the paper win
    if (player_1 == 'paper') and (comp == 'rock'):
        score1 += 1
    # if the player choose scissors and other choose paper
    # then the paper win
    if (player_1 == 'scissors') and (comp == 'paper'):
        score1 += 1
    # if the player choose scissors and other choose rock
    # then the rock win
    if (player_1 == 'scissors') and (comp == 'rock'):
        score2 += 1
    # if the player choose paper and other choose scissors 
    # then the scissors
    if (player_1 == 'paper') and (comp == 'scissors'):
        score2 += 1
    # if the player choose rock and other choose paper
    # then the paper win
    if (player_1 == 'rock') and (comp == 'paper'):
        score2 += 1
    return score1, score2

# asking if player wants to play 
# with computer or player 2
choices = input('computer or player 2?')
# if the player choice computer
if choices == 'computer':
    # begin the game
    print("Let's Play!" )
    while n > 0:
        # the player choose the rock, paper or scissors
        player_1 = input('rock/paper/scissors? ')
        # random choice for computer
        comp = random.choice(lst)
        # show what computer choose
        print(f"computer choose {comp}")
        # call the rules function for the rules of the game
        player_1_score, comp_score = rules(player_1, comp)
        n -= 1
    # make a condition for score
    if player_1_score > comp_score:
        print('You Win!')
        print(f'Your score {player_1_score}')
    else:
        print('You Lose!')
elif choices == 'player 2':
    # begin the game
    print("Let's Play!")
    while n > 0:
        # the player 1 choose the rock, paper or scissors
        player_1 = input('rock/paper/scissors? ')
        # the player 2 choose the rock, paper or scissors
        player_2 = input('rock/paper/scissors? ')
        # call the rules function for the rules of the game
        player_1_score, player_2_score = rules(player_1, player_2)
        n -= 1
    # make a condition for score 
    if player_1_score > player_2_score:
        print('Player 1 Win!')
        print(f'Player 1 score {player_1_score}')
    else:
        print('Player 2 Win!')
        print(f'Player 2 score {player_2_score}')