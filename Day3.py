#Condition FLow and Logical Operators

weight = int(input('Enter your Weight'))
height = float(input('Enter your Height'))
bmi = (weight/(height**2))
if bmi<18.5:
    print('You are UnderWeight')
elif bmi<24.9:
    print('You are Healthy!!!')
elif bmi<29.9:
    print('You are OverWeight')
elif bmi<39.9:
    print('You are Obese')
else:
    print('You are Severely Obese')


#Leap Year
year = int(input('Enter Year '))
if year%400==0 or (year%100!=0 and year%4==0):
    print(f'{year} is a leap year')
else:
    print(f"{year} is not a leap year")


#Logical Opeartors
#and
#or
#not

#Love Calculator
name1 = input('Enter Name 1 ')
name2 = input('Enter Name 2 ')
findstring = 'truelove'
count1=0
count2=0
for i in range(0,len(findstring)):
    count1 += name1.lower().count(findstring[i])
    count2 += name2.lower().count(findstring[i])
if((count1*10)+count2>50):
    print("You are Compatible")
print(f"Counts are {count1} and {count2}")

#Final Project

print('Welcome to Treasure Island')
print('Your mission is to find the treasure ')
direction = input('Which Direction ?? R for Right or Left ').lower()
if direction =='left':
    activity = input('what would you like to do swim or wait?? ').lower()
    if activity =='wait':
        door = input('which door would you like to open?? Red ,Blue or Yellow ').lower()
        if door =='yellow':
            print('You Win!!')
        else:
            print('Game Over!!')
    else:
        print('Game Over!!')
else:
    print('Game Over!!')
