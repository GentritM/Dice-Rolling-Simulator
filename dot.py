import random
import time

def times():
    print("The game started\nDie rolling in: ")
    for i in range(1,4):
        print(i)
        time.sleep(1)
times()

res = []

def roll(tam = 0):
    rand_num = random.randint(1,6)

    while True:
        print("Your score is: ", rand_num)
        user = input("wanna roll the die again?: (y/n) ")


        if user == 'y':
            res.append(rand_num)
            print("Your Die is rolling...")
            for j in range(1,4):
                print(j)
                time.sleep(1)
            return roll()


        elif user == 'n':
            res.append(rand_num)
            print("you played ", len(res), " times")
            print("your results are: ", res, "\nYour total is:", sum(res), "and your average is: ", sum(res)/len(res))
            return "Thanks for playing"


print(roll())
