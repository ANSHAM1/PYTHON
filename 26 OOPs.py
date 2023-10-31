import time

class player:
    def __init__(self,name,health,stamina):
        self.name=name
        self.health=health
        self.stamina=stamina
    
    def p_run(self,run):
        self.run=run
        print()
        print(f"{self.name}'s stamina is {self.stamina}")
        print(f"{self.name}'s health is {self.health}")
        print()
        print(f"{self.name} is running")
        print()
        time.sleep(0.01)
           
        for i in range(self.run):
            self.stamina-=1
            
            if self.stamina>0 and self.stamina<40:
                self.health-=1
                if self.health<=0:
                    print(f"{self.name} died")
                    break
                print(f"{self.name}'s health is {self.health}")
                time.sleep(0.5)
                
            elif self.stamina==0:
                self.health-=10
                if self.health<=0:
                    print(f"{self.name} died")
                    break
                print(f"{self.name} stoped running")
                time.sleep(0.5)
                x=int(input("press 1 if want to force the player to run: "))
                if x==1:
                    self.health-=20
                    self.stamina=1
                    if self.health<=0:
                        print(f"{self.name} died")
                        break
                    else:
                        print(f"{self.name}'s health is {self.health}")
                        time.sleep(0.5)
                else:
                    break
    
    def p_still(self,still):
        self.still=still
        print()
        print(f"{self.name}'s stamina is {self.stamina}")
        print(f"{self.name}'s health is {self.health}")
        print()
        print(f"{self.name} is still")
        print()
        for i in range(self.still):
            self.stamina+=1
            time.sleep(0.3)
            if self.stamina<=40:
                print(".",end="")
            elif self.stamina>40:
                self.health+=2
                print(f"{self.name}'s health is {self.health}")
                time.sleep(0.5)
                if self.health==100:
                    print(f"{self.name}'s health is maxed")
                    break
            elif self.stamina>80:
                self.health+=4
                print(f"{self.name}'s health is {self.health}")
                time.sleep(0.5)
                if self.health==100:
                    print(f"{self.name}'s health is maxed")
                    break
                  
            
player1=player("p1",100,100)

while True:
    print()
    run=int(input("enter the no of meter the player will run: "))
    still=int(input("enter the no of seconds the player will be still: "))
    print()
    player1.p_run(run)
    player1.p_still(still)
    if run<=0 and still<=0:
        break



            
    
    
        
        
            
        