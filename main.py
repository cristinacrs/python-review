import random

options = ('rock', 'paper', 'scissors')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10, '\n')

    user_option = input('Rock, scissors or paper? ')
    user_option = user_option.lower()
    computer_option = random.choice(options)

    rounds += 1

    print('User score: ', user_wins, '\n')
    print('Computer score: ', computer_wins, '\n' )

    if not user_option in options:
        print('Invalid choice !!', '\n')
        continue

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Tie!', '\n')
    elif user_option == 'rock':
        if computer_option == 'scissors':
            print('You have won!', '\n')
            user_wins += 1 
        else:
            print('Sorry, paper wins vs rock!', '\n')
            computer_wins += 1
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('paper wins vs rock')
            print('You have won!', '\n')
            user_wins += 1 
        else:
            print('Sorry, scissors wins vs paper!', '\n')
            computer_wins += 1
    elif user_option == 'scissors':
        if computer_option == 'paper':
            print('Scissors wins vs paper')
            print('You have won!', '\n')
            user_wins += 1 
        else:
            print('Sorry, rock wins vs scissors!', '\n')
            computer_wins += 1

    if computer_wins == 2:
        print('*' * 10)
        print('The computer has won!', '\n')
        break

    if user_wins == 2:
        print('*' * 10)
        print('The user has won!', '\n')
        break

