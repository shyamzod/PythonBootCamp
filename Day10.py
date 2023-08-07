#calculator
def giveoperation(symbol):
    """This functions returns the function name according to symbol"""#This is the Doc String
    operations = {
        '+':Add,
    '-':Subract,
    '*':Multiply,
    '/':Divide}
    return operations[symbol]

def Add(a,b):
    return a+b
def Subract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    return a/b
firstnumber = int(input('Enter first number '))
symbol = input('Enter the operation you want to do ')
secondnumber = int(input('Enter second number '))
methd = giveoperation(symbol)
print(methd(firstnumber,secondnumber))