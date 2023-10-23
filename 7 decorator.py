def greet(fx):
    def mfx(*a,**k):
        print("hello")
        fx(*a,**k)
        print("thanks")
    return mfx

@greet
def add(a,b):
    print(a+b)

add(4,7)