#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SHARJEEL
#
# Created:     27/02/2024
# Copyright:   (c) SHARJEEL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
store=[]
roll=0
result=''


while True:
    try:
        sides=int(input("Enter sides of dice (must be between 1-6) : "))
        if sides>=1 and sides<=6:
            break
        else:
            print("Enter a number between 1 and 6")
    except ValueError:
        print("")

while True:
    try:
        turns = int(input("Enter number of rolls (must be between 1-6): "))
        if turns>=1 and turns<=6:
            break
        else:
            print("Enter a number between 1 and 6")
    except ValueError:
        print("Invalid input. Please enter a number.")



for i in range(1,turns+1):
    store.append(random.randint(1,sides))

for i in store:
    result=result+str(i)


print(f"Number: {result}  ")





