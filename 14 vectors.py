class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def vec(self):
        return f"{self.x}i+{self.y}j+{self.z}k"
    def __add__(self,a):
        x=self.x+a.x
        y=self.y+a.y
        z=self.z+a.z
        print(f"{x}i+{y}j+{z}k")
        return vector(x,y,z)
    def __sub__(self,a):
        x=self.x-a.x
        y=self.y-a.y
        z=self.z-a.z
        print(f"{x}i+{y}j+{z}k")
        return vector(x,y,z)
    
v1=vector(1,1,1)
v2=vector(5,8,9)
v3=vector(6,4,2)
v1+v2-v3



    

