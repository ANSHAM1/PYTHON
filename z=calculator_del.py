print("===========================================================CALCULATOR===========================================================")
print("choices for calculations")
print(" 1 for addiion\n 2 for subtraction\n 3 for division\n 4 for multiplication\n -->hist to check history\n -->exit to end")
l=["---empty---"]
while True:
    m=input("enter your choice: ")
    if m=='hist':
        if len(l)!=1:
            if "---empty---" in l:
                l.remove("---empty---")        
        print("--------------------=history=--------------------")
        for i in range(len(l)):
            print(f"{i+1}. {l[i]}")
        print("----------------------=end=----------------------")
    elif m=='exit':
        break
    else:
        n1=int(input("enter first no: "))
        n2=int(input("enter second no: "))
        match m:
            case '1':
                print(f"{n1}+{n2}={n1+n2}")
                l.append(f"{n1}+{n2}={n1+n2}")
            case '2':
                print(f"{n1}-{n2}={n1-n2}")
                l.append(f"{n1}-{n2}={n1-n2}")
            case '3':
                print(f"{n1}/{n2}={n1/n2}")
                l.append(f"{n1}/{n2}={n1/n2}")
            case '4':
                print(f"{n1}*{n2}={n1*n2}")
                l.append(f"{n1}*{n2}={n1*n2}")
print("===========================================================END OF CODE===========================================================")