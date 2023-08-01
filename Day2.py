
#
number = input('Enter a Number ')
length=len(number)
result=0
for i in range(0,length):
    result+=(int(number[i]))
print('Result is  ' + str(result));

#Mathematical Operators
print(3+2)#Addition
print(3-2)#Subraction
print(3*2)#Product
print(6/2)#Division
print(2**3) # Exponent(Power)


# #BMI Calculator
height = float(input('Enter your height in m : '))
weight = float(input('Enter your weight in kg : '))
bmi = weight/(height**2)
print('The BMI is  : ' + str(round(bmi,2)))

#Coding Excercise 2
age = int(input('Enter your Age'))
remaining_Age = 90-age
remaining_months = int(remaining_Age*12);
remaining_weeks = int(remaining_Age*52)
remaining_days = int(remaining_Age*365)


print(f"You have {remaining_days} days,{remaining_weeks} weeks,and {remaining_months} months left")

#Final Project of Day 2
#Tip Calculator
print('Welcome to the Tip Calculator\n')
total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10,12 or 15?'))
no_of_people_to_split_bill = int(input('How many people to split the bill?'))
result = (total_bill+((total_bill*tip_percentage)/100))/no_of_people_to_split_bill
print(f'Each person should pay: ${round(result,2)}')