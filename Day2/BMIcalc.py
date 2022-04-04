def BMI(weight = float(input("What's your weight in kg \n")), 
        height = float(input("What's your height in meters \n"))):
    nums = round(weight/height**2, 0)
    return nums

print(BMI(), 'is your BMI, welcome')
