import random

def generate_one(string_len):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(string_len):
        res += alphabet[random.randrange(27)]
    return res

def score(goal, test_string):
    num_same = 0
    for i in range(len(goal)):
        if goal[i] == test_string[i]:
            num_same += 1
    return num_same / len(goal)

def main():
    goal_string = "methinks it is like a weasel"
    new_string = generate_one(28)
    best = 0
    new_score = score(goal_string, new_string)

    while  new_score < 1:
        if new_score > best:
            print(new_string, new_score)
            best = new_score
        new_string = generate_one(28)
        new_score = score(goal_string, new_string)

main()
        