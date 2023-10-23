import tkinter as tk

main=tk.Tk()

canvas=tk.Canvas(main)
canvas.pack(side="top", fill="both", expand=True)
canvas_id = canvas.create_text(10, 10, anchor="nw")

#canvas.insert(canvas_id,0," 1 for addiion\n 2 for subtraction\n 3 for division\n 4 for multiplication\n -->hist to check history\n -->exit to end")

def show_num():
    canvas.insert(canvas_id,0," 1 for addiion\n 2 for subtraction\n 3 for division\n 4 for multiplication\n -->hist to check history\n -->exit to end")
    main.after(1000,show_num)

'''
add=tk.Button(main,text="add",bg='red').pack()
sub=tk.Button(main,text="sub").pack()
div=tk.Button(main,text="div").pack()
mul=tk.Button(main,text="mul").pack()
hist=tk.Button(main,text="history").pack()
exit=tk.Button(main,text="exit").pack()
'''

show_num()


main.mainloop()

