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


import random

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','o','p','q','r','s','t','u','v','w','x','y','z']
capital=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers=['1','2','3','4','5','6','7','8','9','0']
char=['&',"*","%","$","#","@"]

password_list=[]

length=int(input("Enter Length:" ))
store=input("Type of Password: easy normal hard: ")


# easy

if(store.lower()=="easy"):
    check=0
    for i in range( int(length/2)):
        password_list.append(random.choice(alphabets))

    for i in range( int(length/2)):
        password_list.append(random.choice(numbers))

    check=length-len(password_list)
    if check>0:
        for i in range(check):
            password_list.append(random.choice(capital))


# normal

elif(store.lower()=='normal'):
    check=0
    for i in range(  int((length* 40) / 100)):
        password_list.append(random.choice(alphabets))
    for i in range( int((length* 20) / 100)):
        password_list.append(random.choice(capital))
    for i in range( int((length* 40) / 100)):
        password_list.append(random.choice(numbers))
    check=length-len(password_list)
    if check>0:
       for i in range(check):
        password_list.append(random.choice(capital))


#hard
elif(store.lower()=="hard"):
    check=0
    for i in range(  int((length* 30) / 100)):
        password_list.append(random.choice(alphabets))
    for i in range( int((length* 30) / 100)):
        password_list.append(random.choice(capital))
    for i in range( int((length* 30) / 100)):
        password_list.append(random.choice(numbers))
    for i in range( int((length* 10) / 100)):
        password_list.append(random.choice(char))
    check=length-len(password_list)
    if check>0:
       for i in range(check):
        password_list.append(random.choice(char))





random.shuffle(password_list)

password=""

for i in password_list:
    password=password+str(i)

print(password)

# formula:
#    Count = (Password Length * Proportion) / 100




