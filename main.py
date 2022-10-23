
import random

name = input("What is your name? ")

print("Hi there, " + name  + ". My name is 2B, your AI helper. How may I assist you today?")

optionchoice = input("A: Nevermind B: My order hasn't arrived.")

continB = "b"

continA = 1

print()

def pconvo():
 optionchoice = input("1: Nevermind 2: My order hasn't arrived.")
if optionchoice.upper == continA.upper:
  print("I see, i'll be here to assist you whenever you need, have a nice day.")
if optionchoice.upper == continB.upper:
  storeinfo = input("To insure, and improve the chat box, and future interactions between clients, will you allow the recording of this conversation. Y/N")


infoPermiY = 'y'

infoPermiN = 'n'

if storeinfo.upper == infoPermiN.upper:
  print("I see.")
  
if storeinfo.upper == infoPermiY.upper:
  print("Thank you for your participation.")

userID = input("What is your User Id.  " )
print()

ConfirmUserId = input(f' {userID}  Y/N ?')

deliverID = input("What was the dilivery ID?")

print("Id found, please wait a moment as we confirm your delivery status.  ")

print('.')
print('.')
print('.')
print('.')