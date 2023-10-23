import tkinter as tk
import time

class real_time():
    def __init__(self):
        self.root=root
        self.label=tk.Label(self.root)
        self.label.pack()
        
        self.time_run()
    def time_run(self):
        self.label.config(text=time.strftime("%H:%M:%S"))
        self.root.after(1000,self.time_run)

root=tk.Tk()
root.geometry("400x400")
r=real_time()
root.mainloop()