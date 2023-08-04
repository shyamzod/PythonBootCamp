import random
#Exercise 1
student_heights = [124,124,125,154,143,173,156]
count = len(student_heights)
sum = 0
for student in student_heights:
    sum+=student
average=sum/count
print(round(average))


#highest score
student_scores = [55,85,83,64,86,99,58]
maxscore=0
for everyscore in student_scores:
    maxscore = max(everyscore,maxscore)
print(maxscore)
print(max(student_scores))

#Adding Even Numbers
endingnumber  = int(input('Enter the number upto which you want to find the sum of even numbers '))
sum=0
for i in range(1,endingnumber+1):
    if i%2==0:
        sum+=i
        print(i)
print(sum)

#FizzBuzz program
limit =  int(input('Enter the upper limit '))
for i in range(1,limit+1):
    if i%3==0 and i%5==0:
        print(f"{i} is a FizzBuzz")
    elif i%3==0:
        print(f"{i} is a Fizz")
    elif i % 5 == 0:
        print(f"{i} is a Buzz")
    else:
        print(i)

#Password Generator
length = int(input('Enter Length of Password '))
password=[]
numbers = int(input('Enter no of Numbers '))
symbolssize = int(input('Enter no of Symbols '))
for i in range(length):
    capitalorsmall = random.randint(0,1)
    if capitalorsmall==0:
        password.append(chr(random.randint(97,122)))
    else:
        password.append(chr(random.randint(65, 90)))
list=[]
symbols = ['&','@','*','!','%','$']
while(numbers>0):
    a= random.randint(0,length-1);
    while(a in list):
        a=random.randint(0,length)
    password[a]=str(random.randint(0,9))
    numbers-=1
    list.append(a)
print(list)
while(symbolssize>0):
    a= random.randint(0,length-1);
    while(a in list):
        a=random.randint(0,length-1)
    password[a]=random.choice(symbols)
    symbolssize-=1
    list.append(a)
print("".join(password))