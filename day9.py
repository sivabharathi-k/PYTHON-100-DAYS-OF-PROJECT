import random
rock='''
_______
---   ____)
      (_)
      (_)
      ()
---.(_)
ROCK'''
paper='''_______
---'    ___)___
           ______)
          _______)
         _______)
---.)
PAPER '''
scissor=''' _______
---'   ___)___
          ______)
       __________)
      ()
---.(_)
SCISSORS'''
lt=[rock,paper,scissor]
import random
user=int(input("Enter a number0,1,2\n"))
print(lt[user])
if(user<0 or user>2):
    print("invaild")
computer=random.randint(0,2)
print(f"computer chose:")
print(lt[computer])
if(user==0 and computer==1):
    print("bot win")
if(user==1 and computer==0):
    print("i win")
if(user==0 and computer==2):
    print("i win")
if(user==2 and computer==0):
    print("bot win")
if(user==1 and computer==2):
    print("bot win")
if(user==2 and computer==1):
    print("i win")

    
