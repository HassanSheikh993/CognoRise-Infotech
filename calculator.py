#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SHARJEEL
#
# Created:     24/02/2024
# Copyright:   (c) SHARJEEL 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def calculation(num1,num2):

    if operator=='+':
        print(f"Sum: {num1+num2}")
    elif operator=='-':
         print(f"Subtraction: {num1-num2}")
    elif operator=='*':
         print(f"Multiplication: {num1*num2}")
    elif operator=='/':
         print(f"Division: {num1/num2}")


while True:
    num1=int(input("Enter First Number: "))
    num2=int(input("Enter Second Number: "))
    operator=input("Select : + - * / :")
    calculation(num1,num2)


