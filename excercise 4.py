#!/usr/bin/env python3

#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

number = int(input("Input a number: "))
index = 1
divisor_list = []

while index != number :
    if number % index == 0 : 
        divisor_list.append(index)
    index+=1

print(divisor_list)
