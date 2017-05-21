# this first python code from wm
import random
import os

ture = -1
guess_count = 0
secret = random.randint(1, 10)

print("pleas guess what the ramdom number in my heart")
print("game start")

while ture:

    input_str = input("please input a ‘number’ ")
    guess = int(input_str)

    if guess == secret:
        print(" you win ")
        break
    else:
        if guess < secret:
            print("the number you input is little than guess")
        else:
            print("the number you input is greater than guess")

    guess_count += 1
    if guess_count >= 3:
        print("the number in my heart is %d" % secret)
        print("game over")
        break
os.system("pause")
