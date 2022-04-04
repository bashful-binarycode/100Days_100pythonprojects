def remaining_life(age = int(input("What's your age?\n"))):
    remaining_years = 90 - age
    remaining_days = remaining_years*365
    remaining_weeks = int(round(remaining_days/7, 0))
    remaining_months = int(round(remaining_days/30, 0))
    print(f"You have {remaining_days} days, {remaining_weeks} weeks and {remaining_months} months")


remaining_life()