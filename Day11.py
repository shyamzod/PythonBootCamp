#Black Jack Game
import random
def givecard():
    cardswithvalues = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
    cards = []
    for key in cardswithvalues.keys():
        cards.append(key)
    randvalue = random.choice(cards)
    return cardswithvalues[randvalue]
print('Welcome to BlackJack Game ')
print('Player Cards')
player=[]
for i in range(0,2):
    player.append(givecard())
print(player)
print('Computer Cards')
computer=[]
computer.append(givecard())
print(computer)
computer.append(givecard())
playersum=0
for item in player:
    playersum+=item
computersum=0
winner=''
for item in computer:
    computersum+=item
if 21-playersum<21-computersum:
    winner='P'
else:
    winner='C'
choice = input('Choose who is closer to 21 press C for Computer abd P for Player ')
if(choice==winner):
    print('Player Won ')
else:
    print('Computer Won ')