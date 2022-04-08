import random

def i_will_pay(names = input("Input the First Name of People playing the game\n")):
    people =  names.split(' ')
#    the_chosen_one = random.choice(people)
    the_chosen_one = people[random.randint(0,len(people)-1)]
    print(the_chosen_one, 'will pay the bill today')

i_will_pay()