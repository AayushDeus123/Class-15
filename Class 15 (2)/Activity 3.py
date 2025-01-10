#Simple Calculator using FUNCTIONS
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

a = int(input('Enter your first number : '))
b = int(input('Enter your second number : '))
opt = input('Choose your operation :\n 1. Add\n 2. Sub\n 3. Mult\n 4. Div\n')

if opt == 'Add' or opt == 'add':
    print('The sum of the two numbers is :',add(a,b))
elif opt == 'Sub' or opt == 'sub':
    print('The difference between the two numbers is :',sub(a,b))
elif opt == 'Mult' or opt == 'mult':
    print('The multiplication of the two numbers is :',mult(a,b))
elif opt == 'Div' or opt == 'div':
    print('The division between the two numbers is :',div(a,b))
else:
    print('Choose between the given options')