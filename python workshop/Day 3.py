# def add():
#     x=5
#     print(x)
# add()

# x=34
# def function():
    
#     print(x)
# function()

# import random
# def ran():
#    return random.randint(1,100)
# num=ran()
# Noofguess=0
# # print(num)
# while True:
#    m=int(input("Guess the number\n"))
#    Noofguess=Noofguess+1
#    if(num>m):
#       print("Enter higher number please")
#    elif(num<m):
#       print("Enter lower number please")
#    else:
#       print("You win the game")
#       break
# print(f"No of Guess {Noofguess}")      

import random
def roll_dice():
   return random.randint(1,6)
def check():
   num=roll_dice()
   m=int(input("Guess the number\n"))
   # Noofguess=Noofguess+1
   if(num>m):
      print("You loss the game")
   elif(num<m):
      print("Your win the game")
   else:
      print("Game is tie")
print(check())      
      
# print(f"No of Guess {Noofguess}") 



