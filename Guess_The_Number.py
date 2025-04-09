import random

class Guess_number:
    def __init__(self,computer,you,i):
        self.computer=computer
        self.you=you
        self.i=i
        
    def find(self):
        while(self.i<11):
            
            if(self.you==self.computer):
                print("\nYou Successfully Guess The NUmber!!")
                break
            
            elif(self.you<self.computer):
                print(f"\nYour Chance NO {self.i}")
                print("Your Guess Number is less Then Computer Guess Number!")
                self.you=int(input("Enter Your Number for Next Chance:"))
                
            elif(self.you>self.computer):
                print(f"\nYour Chance NO {self.i}")
                print("Your Guess Number is Greater Then Computer Guess Number!")
                self.you=int(input("Enter Your Number for Next Chance:"))
            
            self.i +=1
            
        else:
            print("\nBetter Luck Next Time!!")
            print(f"Computer Guess Number is: {self.computer}")
        
print("You have 10 Chance for Guess The Number")      
print("Your Chance No 1")  
Number=Guess_number(random.randint(1,100),int(input("Enter Your Number Between {1-100}:")),2)
Number.find()