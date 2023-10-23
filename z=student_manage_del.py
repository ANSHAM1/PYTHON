def view_student(l):
    for ind,i in enumerate(l):
        print(f"{ind+1}.{i}")

def add_student(l):
    name=input("enter name of student: ")
    age=int(input("enter age of student: "))
    grade=input("enter grade of student: ")
    n=[name,age,grade]
    l.append(n)
    

def remove_student(l):
    n=int(input("enter index of task which is to remove"))
    temp=(l.pop(n))[0]
    return (f"{temp} is removed")
    
def search_student(l):
    n=input("enter name of student: ")
    c=0
    for i in l:
        if n==i[0]:
            print(i)
            c=c+1
    if c==0:
        print("student not found")
            



    
print("===========================================================STUDENT MANAGER===========================================================")
print(" available choices are: ")
print(" 1 add_student\n 2 for remove_student\n 3 to view student\n 4 to search_student\n 5 to end")
print()
l=[]
while True:
    n=input("enter your choice: ")
    match n:
        case '1':
            add_student(l)
        case '2':
            print(remove_student(l))
        case '3':
            view_student(l)
        case '4':
            search_student(l)
        case '5':
            break
print("===========================================================END OF CODE===========================================================")
    
    
    