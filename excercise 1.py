#!/usr/bin/env python3
#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
#Extras:
#- Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#- Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)


from datetime import date

current_year_string = date.today().year
name = input("Enter your name: ")
age = int(input("Enter your age: "))

def create_message() :
    return name + ", you will turn 100 the following date: " + calculate_year()

def calculate_year() : 
    return str(current_year_string + (100 - age))

print(create_message())

for x in range(0,int(input("Give me another number: "))) :
    print(create_message() + "\n")


