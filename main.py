import random

options = ('rock', 'paper', 'scissors')

user_option = input('Rock, scissors or paper? ')
user_option = user_option.lower()
computer_option = random.choice(options)

if not user_option in options:
    print('Invalid choice !!')

print('User option =>', user_option)
print('Computer option =>', computer_option)

if user_option == computer_option:
    print('Tie!')
elif user_option == 'rock':
    if computer_option == 'scissors':
        print('You have won!')
    else:
        print('Paper wins vs rock!')
elif user_option == 'paper':
    if computer_option == 'rock':
        print('paper wins vs rock')
        print('You have won!')
    else:
        print('scissors wins vs paper!')
elif user_option == 'scissors':
    if computer_option == 'paper':
        print('Scissors wins vs paper')
        print('You have won!')
    else:
        print('Rock wins vs scissors!')

