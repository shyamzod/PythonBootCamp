# Coffee Machine
resources = {'Water': 300,
             'Milk': 200,
             'Coffee': 100,
             'Amount':0}
requirements = {'Espresso': {'Water': 50,
                             'Milk': 0,
                             'Coffee': 18},
                'Latte': {'Water': 200,
                          'Milk': 150,
                          'Coffee': 24},
                'Capaccuino': {'Water': 250,
                               'Milk': 100,
                               'Coffee': 24}
                }

costs = {
    'Espresso': 1.50,
    'Latte': 2.50,
    'Capaccuino': 3.00
}


def report():
    print(f"Water {resources['Water']} ml, Milk {resources['Milk']} ml,Coffee {resources['Coffee']} g and Amount ${resources['Amount']}")


def decidechoice(choice):
    if choice == 'report':
        report()
    elif choice == 'coffee':
        makecoffee()


def makecoffee():
    giveoptions()
    option = int(input('Choose by typing the corresponding number'))
    if option == 1:
        make('Espresso')
    elif option == 2:
        make('Latte')
    elif option == 3:
        make('Capaccuino')
    else:
        print('Invalid Option')


def make(choice):
    target = costs[choice]
    print('Please insert coins ')
    penny = int(input('Enter the pennys '))
    dime = int(input('Enter the Dime '))
    nickel = int(input('Enter the Nickel '))
    quarter = int(input('Enter the Quarter '))
    total = (penny * 0.01) + (dime * 0.10) + (nickel * 0.05) + (quarter * 0.25)
    resourcesavailable = checkresources(choice)
    if total >= target and resourcesavailable:
        print(f'please have this {choice}')
        resources['Amount']+=costs[choice]
        deductresources(choice)
        if total > target:
            print(f'please take the change {total - target}')
    else:
        if not resourcesavailable:
            print(f"Resources not available please take your refund of ${round(total,2)}")
        elif total<target:
            print(f"Your inserted amount is lower than {choice} cost which is ${costs[choice]} ")


def checkresources(choice):
    return (resources['Water']>=requirements[choice]['Water']) and (resources['Coffee'] >= requirements[choice]['Coffee']) and (resources['Coffee'] >= requirements[choice]['Coffee'])


def deductresources(choice):
    resources['Water'] -= requirements[choice]['Water']
    resources['Coffee'] -= requirements[choice]['Coffee']
    resources['Milk'] -= requirements[choice]['Milk']


def giveoptions():
    print('What would you like to have ')
    print('1.Espresso')
    print('2.Latte')
    print('3.Capaccuino')



#Main Program
exitprogram = False
while not exitprogram:
    choice = input('Please Enter what you want to do (report/coffee) ')
    decidechoice(choice)
    wanttoExit = int(input('1 for exit and 0 for not '))
    if wanttoExit == 1:
        exitprogram=True

