print("Welcome to Treasure Island, Your Mission is to find the treasure.")
def play():
    story = ['Left', 'Wait', 'Yellow']
    options = ['Left or Right ', 'Swim or Wait ', 'Which Door? Blue, Yellow, Red ']
    result = ["Your fate took a wring turn","Well you are not a good swimmer","Sorry the door you chose gave you death instead"]
    
    for _ in range(0,3):
        if input(options[_]+" ").capitalize() != story[_]:
            print("Game Over! "+ result[_])
            exit()
        else :
            print("Going Nice ")
    print("You found the treasure!")
    


play()