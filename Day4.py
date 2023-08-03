# #Random Numbers
import random
a = random.randint(1,10)#random number between 1 and 10 and includes 10
b = random.random()#generates between 0.0 to 1.0 random number
print(round(a*b,2))#To print Random Float

#list data structure
list = [] # can store any datatype elements

for i in range(0,10):
    list.append(random.randint(1,10))
list.sort()
list1 = [11,12]
list.extend(list1)#adds whole list at the end of the list
print(list.index(11))#index of particular element
list.pop()#removes the element from the list
print(list)

#Banker Roulette coding Exercise
names = input('Enter the Names ')
nameslist = names.split(',')
choice = random.randint(0,len(nameslist)-1)
print(nameslist[choice])
print(random.choice(nameslist))#it chooses a element from random index and list is passed as argument

#Treasure Map Exercise
list1 = ['😊','🤣','🥰']
list2 =['🤨','🤔','🤩']
list3 = ['😣','😥','😮']
map=[list1,list2,list3]
cellinput = input('Enter row and column no ')
print(map[int(cellinput[0])][int(cellinput[1])])

#Day 4 Final Project
#Rock Papers Scissors
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
items = [rock,paper,Scissors]
choice = int(input('What do you Choose ?? 0 for Rock 1 for Paper and 2 for Scissor '))
mychoice = items[choice]
computerchoice = items[random.randint(0,2)]
print(mychoice)
print(computerchoice)
if(mychoice!=computerchoice):
    if mychoice==rock:
        if computerchoice==Scissors:
            print('I Won')
        else:
            print('Computer Won')
    elif mychoice==Scissors:
        if computerchoice==paper:
            print('I Won')
        else:
            print('Computer Won')
    else:
        if computerchoice==rock:
            print('I Won')
        else:
            print('Computer Won')
else:
    print('Draw')
