import pyttsx3

l=eval(input("enter a list of students: "))

engine = pyttsx3.init()
engine.setProperty('volume',40)
engine.setProperty('rate',150)

for i in l:
    engine.say(f"{l}")
engine.runAndWait()
