# Hangman
import math
import random
lifes=3
wordlist = ['Apple','Banana','Mango','Guava','Custard Apple','Kiwi Fruit']
word  = random.choice(wordlist).lower()
print(word)
wordlength = len(word)
blankstoadd = int(math.floor(wordlength*0.5))
wordlistform = []
for ch in word:
    wordlistform.append(ch)
print(wordlistform)
originalwordlist = []
for ch in word:
    originalwordlist.append(ch)
toguessindices = []
while blankstoadd>0:
    randindex = random.randint(0,wordlength-1)
    if randindex not in toguessindices and wordlistform[randindex]!=' ':
        toguessindices.append(randindex)
        wordlistform[randindex]='_'
        blankstoadd-=1
print("".join(wordlistform))
print('Guess the letters ')
print(toguessindices)
won=False
alreadyguessed = []
while lifes>0 and not won:
    guess = input('Enter the guess character ')
    found=False
    for ind in toguessindices:
        if originalwordlist[ind] == guess:
            wordlistform[ind]=guess
            print("".join(wordlistform))
            toguessindices.remove(ind)
            print('Guessed Correct')
            found=True
            break
    if not found and guess not in alreadyguessed:
        print("You Guessed Wrong !! ")
        alreadyguessed.append(guess)
        lifes-=1
    elif guess in alreadyguessed:
        print('You have already guessed this and this is wrong ')
    if '_' not in wordlistform:
        won=True
if won:
    print(f"You have won with {lifes} lives left")
else:
    print(f"You have  {lifes} lives left")
    print('Better Luck Next Time !!')