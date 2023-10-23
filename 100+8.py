import tkinter as tk
import random 

class slideshow():
    def __init__(self,rang):
        self.rang=rang
        self.list=[]
        self.current_num=0
        self.game=["snake","water","gun"]

        self.outcome=[["DRAW","LOSS","WIN"],
                      ["WIN","DRAW","LOSS"],
                      ["LOSS","WIN","DRAW"]]
        
        self.canvas=tk.Canvas(root)
        self.canvas.pack(side="top", fill="both", expand=True)
        self.canvas_id = self.canvas.create_text(10, 10, anchor="nw")

    def ran_of(self,user):
        self.user=user   
        sys=random.randint(0,2)
        sys_val=self.game[sys]
        self.canvas.insert(self.canvas_id,0,f"-------------------------\nyour choice={self.game[user-1]}\nsystem choice={sys_val}\nresult={self.outcome[sys][self.user-1]}\n")
    
root=tk.Tk()
slideshow = slideshow(100)
while True:
    user=int(input("enter integer: 1.snake, 2.water ,3.gun, 0 is want to exit: "))
    if user in [1,2,3]:
            preview=slideshow.ran_of(user)
    else:
        break
root.mainloop()

