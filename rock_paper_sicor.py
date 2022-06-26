import random

user_Wins =0
computer_wins = 0

options =["rock","paper","scissors"]


while True:
    user_input =input("Plaese Enter Rock/Paper/Scissors or q to quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue

    random_number =random.randint(0,2)
    #rock 0, paper 1,scissors 2
    computer_picks = options[random_number]
    if user_input =='rock' and computer_picks =='scissors':
        print('You Won')
        user_Wins+1
    elif user_input =='scissors' and computer_picks == 'paper':
        print('you Won')
        user_Wins+1 
    elif user_input == 'paper' and computer_picks =='rock':
        print('you Won')
        user_Wins+1
    else :
        print(random_number)
        
        print('You Loose')
print("You Won " ,user_Wins ," times")
print('Computer Win ',computer_wins,' times')
print("Good bye !")