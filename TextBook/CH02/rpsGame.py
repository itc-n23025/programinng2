import random, sys
print('ROCK, PAPER, SCISSORS')
win = 0
losses = 0
ties = 0

while True:
    print(str(wins)+' Win, '+str(losses)+' Losses, '+str(ties)+' Ties')
    while True:
        print('Enter you move: (r)ock (p)aper (s)ccissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('Type one of r,p,s,or q.')

if player_move == 'r':
    print('ROCK versus...')
elif player_move == 'p':
    print('PAPPER versus...')
elif player_move == 's':
    print('SCISSORS versus...')

random_number = random.randint(1, 3)
if random_number == 1:
    computer_move = 'r'
    print('ROCK')
elif random_number == 2:
    computer_move = 'p'
    print('PAPER')
elif random_number == 3:
    computer_move = 's'
    print('SCISSORS')

if player_move == computer_move:
    print('It is a tie!')
    ties = ties + 1
elif player_move == 'r' and computer_move == 's':
    print('You win!')
    wins = wins + 1
elif player_move == 'p' and computer_move == 'r':
    print('You win!')
    wins = wins + 1
elif player_move == 's' and computer_move == 'p':
    print('You win!')
    wins = wins + 1
elif player_move == 'r' and computer_move == 'p':
    print('You lose!')
    losess = losses + 1
elif player_move == 'p' and computer_move == 's':
    print('You lose!')
    losses == losses + 1
elif player_move == 's' and computer_move == 'r':
    print('You lose!')
    losses = losses + 1