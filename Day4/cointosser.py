import random

def toss(no_of_coins:int):
    for _ in range(1,no_of_coins+1):
        result = random.randrange(0,2)
        heads = 0
        tails = 0
        if result == 0:
            heads+=1
            print(f"Toss number {_}: Heads")
        else:
            tails +=1
            print(f"Toss number {_}: Tails")
    
toss(20)