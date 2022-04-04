def tips(amount: int, no_of_people: int, tip_percentage: int):
    print("Welcome to the tip calculator!")
    per_person = round((amount+((tip_percentage/100)*amount))/no_of_people, 2)
    per_person = "{:.2f}".format(per_person)
    print(f"Your bill is {amount} and with tip percentage of {tip_percentage}%  each person has to pay {per_person}")
tips(500, 6, 12)
