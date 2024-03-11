#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SHARJEEL
#
# Created:     25/02/2024
# Copyright:   (c) SHARJEEL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
game=['rock','paper','scissors']

games_win={
'user':0,
'computer':0}

while True:

    print("++++++++++++++++++++++++++++++++++++++++++")
    print("Press 1 to play game ")
    print("Press 2 to check score ")
    print("Press 3 to stop ")
    print("++++++++++++++++++++++++++++++++++++++++++")
    select=int(input("Enter Choice: "))


    if select==1:


        user_choice=input("Enter (Rock,Paper,Scissors) : ")
        user_choice=user_choice.lower()

        computer_choice=random.choice(game)
        if user_choice=='rock' or user_choice=='paper' or user_choice=='scissors':

            if (computer_choice=='rock' and user_choice=='scissors') or (computer_choice=='scissors' and user_choice=='paper') or(computer_choice=='paper' and user_choice=='rock'):
                print(f"User: {user_choice}  Computer: {computer_choice}")
                print("COMPUTER WINS 😱")
                games_win['computer'] +=1


            elif computer_choice==user_choice:
                print(f"User: {user_choice}  Computer: {computer_choice}")
                print("DRAW")


            else:
                print(f"User: {user_choice}  Computer: {computer_choice}")
                print("TOU WIN 😀")
                games_win['user'] +=1

        else:
            print("Invalid choice Try again 🥺")

    elif select==2:
        for key,val in games_win.items():
            print(key, ':', val)

    elif select==3:
        break

    else:
        print("Invalid Choice 🥺")

