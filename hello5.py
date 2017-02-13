#This program says hello and asks for my name

myName = input('Welcome, What is your name?')
print('Welcome '+ myName)
passWrd = input('What is the password ' + myName)
passWrd=''
while passWrd != 'monty':
        print ('Access Granted!')
        print ('The length of your name is:')
        print (len(myName))
        myAge = input('What is your age? ')
        print ('You will be ' + str(int(myAge) + 1) + ' in a year')
else:
    print('Wrong Password!')
