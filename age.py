#------------------------Age Questions ----------------------  
import random

def myAge(age):
  response3 = random.randint(1, 2)
  
  if age <15:
      if response3 == 1:
          print("You are so young! What are your interests?")
      elif response3 == 2:
          print("That's great that you are still young!")        
  elif age >= 15 and age < 18:
      print("Yeah! You are a teenager! That's crazy!")
  elif age >= 18 and age < 55:
      print("Oh, cool!")
  elif age >= 55 and age<120:
      print("So glad to see you here today!")
  else:
      print("You can't be that old. Try again.")
      age2 = int(input("What is your age?"))
      if age2<120:
        print("Okay! This more like an age number.")


age = int(input("\nWhat is your age? "))
myAge(age)