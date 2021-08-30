"""
Write a function that generates a string that is 28 characters long by choosing random letters 
from the 26 letters in the alphabet plus the space. 

We’ll write another function that will score each generated string by comparing the randomly 
generated string to the goal.

A third function will repeatedly call generate and score, then if 100% of the letters are correct 
we are done. 

If the letters are not correct then we will generate a whole new string. 

To make it easier to follow your program’s progress this third function should print out the best string 
generated so far and its score every 1000 tries.
"""

import random
import string

def generate_string(string_length):
    """Generates string that is n 
    characters long plus a space
    """
    our_string = ""
    for x in range(string_length):
        letter = random.choice(alphabet)
        our_string += letter
    return our_string

def compare_string(goal, our_string):
    score = 0
    for i in range(len(goal)):
        if goal[i] == our_string[i]:
            lis.append(i)
            score += 1
    return score

goal = "aaron"
goal_len = len(goal)

alphabet = string.ascii_lowercase + " "

count = 0
while True:

    our_string = generate_string(goal_len)
    current_score = compare_string(goal, our_string)

    if current_score == goal_len:
        print(our_string, goal_len, current_score)
        break

    count += 1

    if count % 1000 == 0:
        print(count)

