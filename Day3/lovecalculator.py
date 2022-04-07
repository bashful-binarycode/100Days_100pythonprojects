def love(boy = input("Name of the boy\n"), girl = input("Name of the girl\n")):
    list_of_words = [i for i in boy.replace(' ','').lower()] + [_ for _ in girl.replace(' ','').lower()]
    true_count = str(list_of_words.count('t') + list_of_words.count('r') +list_of_words.count('u') +list_of_words.count('e'))
    love_count = str(list_of_words.count('l') + list_of_words.count('o') +list_of_words.count('v') +list_of_words.count('e'))
    percentage = true_count + love_count
    
    if 90<int(percentage) or int(percentage)<10:
        print(f"Your score is {percentage}%, You are like coke and mentos")
    elif 40<int(percentage)<50 :
        print(f"Your score is {percentage}%, You are alright together")
    else:
        print(f"Your score is {percentage}%")
    return int(percentage)
#count method is used when when we need to count an occurence of a data 
love()