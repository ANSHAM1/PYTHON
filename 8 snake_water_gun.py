import random 

game=["snake","water","gun"]

outcome=[["DRAW","LOSS","WIN"],
         ["WIN","DRAW","LOSS"],
         ["LOSS","WIN","DRAW"]]

while True:
    sys=random.randint(0,2)
    sys_val=game[sys]
    user=int(input("enter integer: 1.snake, 2.water ,3.gun, 0 is want to exit: "))
    if user==0:
        break
    print(sys_val)
    print(outcome[sys][user-1])


                    


