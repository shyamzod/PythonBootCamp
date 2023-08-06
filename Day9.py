#Auction Program
import os
dict = {}
more = True
def clr():
    if os.name=='nt':
        os.system('cls')
while more:
    name= input('Enter the Name of the Person ')
    bid  = int(input('Enter your bid $'))
    dict[name]=bid
    more_bids = input('Press E for Exit')
    clr()
    if more_bids == 'E':
        more=False
max1 = 0
winner=""
for key in dict.keys():
    if max1<dict[key]:
        max1=dict[key]
        winner=key
print(f"{winner} has won with a bid of ${bid}")

