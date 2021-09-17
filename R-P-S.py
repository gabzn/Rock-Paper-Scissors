import random

rps = ['rock', 'paper', 'scissors']

while True:
    user_input = input('Rock, Paper, Scissors  (Enter exit/quit to stop) \n').lower()
    if  user_input == 'exit' or user_input == 'quit' or user_input == 'stop':
        print('Thanks for playing!')
        break
    
    bot_choice = rps[ random.randint(0, 2) ]
    print(f'I chose {bot_choice}')

    if user_input == 'rock' or user_input == 'r':
        if bot_choice == 'scissors':
            print('You win!')
        elif bot_choice == 'paper':
            print('You lose!')
        else:
            print("It's a tie!")

    if user_input == 'paper' or user_input == 'p':
        if bot_choice == 'rock':
            print('You win!')
        elif bot_choice == 'scissors':
            print('You lose!')
        else:
            print("It's a tie!")

    if user_input == 'scissors' or user_input == 's':
        if bot_choice == 'paper':
            print('You win!')
        elif bot_choice == 'rock':
            print('You lose!')
        else:
            print("It's a tie!")