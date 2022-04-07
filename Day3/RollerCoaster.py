def total_cost(height = int(input('What is your height?\n')), age = int(input('What is your age?\n'))):
    if height > 120 :
        if age <= 12:
            cost = 5
            print("Your ticket fare would be $5")
        elif age <= 18:
            cost = 7
            print("Your ticket fare would be $7")
        elif 45<= age <= 55:
            cost = 0
            print("This ride would be free for you!")
        else :
            cost = 12
            print("Your ticket fare would be $12")
        answer = input("Would you like a picture? Y / N\n")
        if  answer == "Y":
            cost += 3
            print(f"Your total cost would be ${cost}")
        else:
            print(f"Your total cost would be ${cost}")
    else:
        print("Sorry! you have to grow taller to ride this roller coaster")
# When the function is not called it will not print anything
# Therefore to return outputs and print statements the function has to be called.
# If you use functions here it will run every line of code even if does not make sense. So instead use only one function.
#    want_picture(coaster_cost()) 
total_cost()
