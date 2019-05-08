#!/usr/bin/env python3 

#Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
#Extras:
#- Randomly generate two lists to test this
#- Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

a = random.sample(range(0, 100), random.randint(0,100))
b = random.sample(range(0, 100), random.randint(0,100))

common_entries = []

for number in a :
    if number in b and number not in common_entries :
        common_entries.append(number)	

print(a)
print(b)
print(common_entries)

#Extra's? No clue
