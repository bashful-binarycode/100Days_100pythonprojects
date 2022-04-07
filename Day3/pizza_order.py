def pizza_details(size = input("What size of pizza do you want? S, M, L\n")):
    order = [i for i in size.replace(" ",'').upper()]
    cost = 0
# There is no need for replace method as the for statement will ignore the space, it is there for cleaniness of code
    for i in order:
        if i == "S":
            peperoni = input("Do you want peperoni on small pizza? Y/N\n")
            chesse = input("Do you want extra cheese on small pizza? Y/N \n")
            cost += 15
            if peperoni == 'Y':
                cost += 2
            if chesse == 'Y':
                cost += 1
        if i == "M":
            peperoni = input("Do you want peperoni on meduim pizza? Y/N\n")
            chesse = input("Do you want extra cheese on medium pizza? Y/N \n")
            cost += 20
            if peperoni == 'Y':
                cost += 3
            if chesse == 'Y':
                cost += 1
        if i == "L":
            peperoni = input("Do you want peperoni on large pizza? Y/N\n")
            chesse = input("Do you want extra cheese on large pizza? Y/N \n")
            cost += 25
            if peperoni == 'Y':
                cost += 3
            if chesse == 'Y':
                cost += 1
    count_small_pizza = order.count("S")
    count_medium_pizza = order.count("M")
    count_large_pizza = order.count("L")
    print(f"Your order is {count_small_pizza} Small Pizza, {count_medium_pizza} Medium Pizza and {count_large_pizza} Large Pizza.\n Your final bill: {cost}")   
pizza_details()