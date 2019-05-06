#!/usr/bin/env python 
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
#
#Extras:
#-If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = float(input("input a number: "))

if number % 4 == 0 :
    print("This number is a multiple of four!")
elif number % 2 == 0 : 
    print("You've entered an even number!")
else : 
    print("You've entered an uneven number!") 

num = int(input("Input first number: "))
check = int(input("Input second number: "))

if num % check == 0 :
    print("Check divides equally into num!")
else : 
    print("Check does not divide equally into num!")
