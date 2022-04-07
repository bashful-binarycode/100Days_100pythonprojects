def findit(a):
    if type(a) != int:
        print('Please provide a whole number')
        return False
    elif a % 2==0:
        print('This is an even Number')
        return True
    else:
        print("This is an odd Number")
        return False

if (findit(66)):
    print('Findit has returned the value')