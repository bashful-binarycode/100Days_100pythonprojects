import random
comp_choice = random.choice(['Rock','Paper','Scissor'])
rounds = int(input("How many rounds would you like to play? "))

comp_score = 0
user_score = 0

for i in range(0,rounds):
    user_choice = input("'Rock' or 'Paper' or 'Scissor' ").capitalize()    
    if comp_choice == user_choice :
        print("It's a draw!")
    elif comp_choice == 'Rock' and user_choice != 'Paper':
        print(f'Computer chose {comp_choice.upper()}, you lose!')
        comp_score += 1
    elif comp_choice == 'Rock' and user_choice == 'Paper':
        print(f'Computer chose {comp_choice.upper()}, you win!')
        user_score += 1
    elif comp_choice == 'Paper' and user_choice != 'Scissor':
        print(f'Computer chose {comp_choice.upper()}, you lose!')
        comp_score += 1
    elif comp_choice == 'Paper' and user_choice == 'Scissor':
        print(f'Computer chose {comp_choice.upper()}, you win!')
        user_score += 1    
    elif comp_choice == 'Scissor' and user_choice != 'Rock':
        print(f'Computer chose {comp_choice.upper()}, you lose!')
        comp_score += 1
    elif comp_choice == 'Scissor' and user_choice == 'Rock':
        print(f'Computer chose {comp_choice.upper()}, you win!')
        user_score += 1
print(f'Your score = {user_score}', f'computer score = {comp_score}' )