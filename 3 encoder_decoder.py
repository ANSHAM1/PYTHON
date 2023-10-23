message=input("enter your message: ")
print("-"*100)
print("this is the code: ")
print("---->")
print()
words=message.split()
encodedlist=[]
decodedlist=[]
w_dict={"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","j":"q","k":"p",
        "l":"o","m":"n","n":"m","o":"l","p":"k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e",
        "w":"d","x":"c","y":"b","z":"a","1":"!","2":"@","3":"#","4":"$","5":"%","6":"^","7":"&",
        '8':"*",'9':"(",'0':")","!":'1',"@":'2',"#":'3',"$":'4',"%":'5',"^":'6',"&":'7',"*":'8',
        "(":'9',")":'0',',':'~','~':','}

#encoder
for i in words:
    for j in i:
        encodedlist.append(w_dict[j])
    encodedlist.append(" ")
for a in encodedlist:
    print(f"{a}",end="") 
print()

#decoder
for i in encodedlist:
    if i==" ":
        decodedlist.append(" ")
    else:
        decodedlist.append(w_dict[i])
for a in decodedlist:
    pass
    print(f"{a}",end=(""))
    



