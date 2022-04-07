def leapyear(year = int(input("Put the year you want to check\n"))):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                print("This is a leap year")
            else:
                print("Not a Leap year")
        else:
            print("This is a leap year")
            
    else:
        print("Not a Leap year")

leapyear()