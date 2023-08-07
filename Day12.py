#The Number Guessing Game
import random
def givelives(level):
    levels = {'easy':10,'hard':5}
    return levels[level]
level = input('Choose the level easy or hard ')
lives = givelives(level)
targetvalue = random.randint(1,100)
while lives>0:
    guess = int(input('Make a guess '))
    if guess<targetvalue:
        print('Your guess is low ')
    elif guess>targetvalue:
        print('Your guess is high ')
    else:
        print('You Won!! You guessed the correct value ')
        break
    lives-=1
    print(f"You have {lives} left! ")