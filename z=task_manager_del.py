def to_do_list(l):
    for ind,i in enumerate(l):
        print(f"{ind+1}.{i}")

def add_task(l):
    n=input("enter a task to do: ")
    l.append(n)
    

def remove_task(l):
    n=int(input("enter index of task which is to remove"))
    l.pop(n)

    
    
print("===========================================================TASK MANAGER===========================================================")
print(" available choices are: ")
print(" 1 for to_do_list\n 2 for add_task\n 3 for remove_task\n 4 to end")
print()
l=[]
while True:
    n=input("enter your choice: ")
    match n:
        case '1':
            to_do_list(l)
        case '2':
            add_task(l)
        case '3':
            remove_task(l)
        case '4':
            break
print("===========================================================END OF CODE===========================================================")
    
    
    
    
    
    
    
    
    
    
