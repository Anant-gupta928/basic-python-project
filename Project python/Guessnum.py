import random
target = random.randint(1,100)
while True:
      userchoice = (input("guess the target value or Quit to press (Q):"))
      if(userchoice== "Q"):
            break
      userchoice = int(userchoice)
      if (userchoice == target):
            print("Success: correct guess!")
            break
      elif(userchoice<target):
            print("please write again some bigger value ")
      else:
            print("please write again some smaller value")  


print("________GAME OVER____________")