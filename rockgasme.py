import random
user=int(input("enter input as 0:rock,1:paper,2:sessior"))
if user>=3 or user<0:
    print("invalid number")
computer=random.randint(0,2)
print("computer no choice is",computer)           
if computer==user:
    print("draw")
elif computer==2 and user==0:
    print("you win")
elif user==2 and computer==0:
    print("you lose")
elif user>computer:
    print("you win")
elif computer>user:
    print("you lose")    