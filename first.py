# this first python code from wm
import random

game_end = -1
guess_count = 0
secret = random.randint(1, 10)

print("pleas guess what the ramdom number in my heart")
print("game start")

while game_end and guess_count < 3:

    input_str = input("please input a ‘number’ ")
    guess = int(input_str)

    if guess == secret:
        game_end = 0
        print(" you win ")
    else:
        if guess < secret:
            print("the number you input is little than guess")
        else:
            print("the number you input is greater than guess")

    guess_count = guess_count + 1

if guess_count >= 3:
    print("the number in my heart is %d" % secret)
    print("game over")
input("please enter any key to quit")
