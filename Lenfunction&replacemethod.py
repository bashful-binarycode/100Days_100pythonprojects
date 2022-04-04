#count the number of alphabets in a word
def counter(a = input("Give me a word.\n")):
    print(len(a.replace(' ', '')))

counter()