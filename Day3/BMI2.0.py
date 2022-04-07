def BMI(weight = float(input("What's your weight in kg \n")), 
        height = float(input("What's your height in meters \n"))):
    nums = round(weight/height**2, 1)

    def health(a):
        if a < 18.5:
            print('Underweight')
        elif a < 25:
            print("Normal Weight")
        elif a < 30 :
            print("Over Weight")
        elif a < 35 :
            print( "Obese")
        else :
            print("CLinically Obese")
    
    health(nums)

BMI()
