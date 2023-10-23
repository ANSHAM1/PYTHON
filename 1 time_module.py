import time
t=int(time.strftime('%H'))
if (t>0 and t<5)or(t>19 and t<24):
    print("good night")
elif t>5 and t<12:
    print("good morning")
elif t>12 and t<16:
    print("good after noon")
elif t>16 and t<19:
    print("good evening")

