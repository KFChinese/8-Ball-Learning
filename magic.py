# Created by Larry Chiem
# Date:1/6/20
# Puepose: This is for building a magic 8 ball
# that will see if my RNG skills is any Good. "OOF".

import responses as responses
import time
import random
import os


def eightball():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the Magic 8 ball!")
    print("*" * 35)
    print("")
    time.sleep(.5)
    input("What is your question? \nAnswer it here: ")

    print("Shaking...")
    time.sleep(1)
    print("The 8 Ball Has Spoken!\nYour answer to your question is: " +
          random.choice(responses.response))
    print("")
    time.sleep(1)


while True:
    eightball()
    restart = input("Do you want to restart the 8Ball? \nY/N?: ")
    time.sleep(1)
    if restart == "N":
        break
    elif restart == "n":
        break
    elif restart == "Y":
        continue
    elif restart == "y":
        continue
