class myclass:
    def __init__(self,v):
        self.value=v

    def show(self):
        print("hello world")
    
    @property
    def val(self):
        return 10*self.value+6
    
    @val.setter
    def val(self,newval):
        self.value=newval//3
    
obj=myclass(34)
print(obj.val)
obj.val=55
print(obj.val)    