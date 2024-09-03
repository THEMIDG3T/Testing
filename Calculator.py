#import time to allow reading time
import time

#Print title
print("Two Number Python Calculator")
time.sleep(0.2)

#set numerical inputs
num1 = int(input("What is your 1st number"))

time.sleep(0.2)

num2 = int(input("What is your 2nd number"))
time.sleep(0.5)

#ask if they want to do multiplication
Multiplication = str(input("Would you like to do Multiplication?"))
time.sleep(0.5)

#Multiplication

if Multiplication == 'yes':
    total = num1*num2
    print(total)

# if yes or no isnt inputted then error message and exit
if Multiplication != 'yes' or 'no':
    print("Error")
    exit()

#else ask if they want to do division
else:
    Division = str(input("Would you like to divide your two numbers"))
if Division == 'yes':
    total = num1/num2
    print(total)
    
# if yes or no isnt inputted then error message and exit
if Division != 'yes' or 'no':
    print("Error")
    exit()

    time.sleep(0.5)
    
# else ask if they want to subtract their two numbers
else:
    Subtraction = str(input("Would you like to subtract your two numbers"))
if Subtraction =='yes':
    total = num1-num2
    print(total)

# if yes or no isnt inputted then error message and exit
if Addition != 'yes' or 'no':
    print("Error")
    exit()
# else ask if they want to add their two numbers
else:
    Addition = str(input("Would you like to subtract your two numbers"))
if Addition =='yes':
    total = num1+num2
    print(total)
# if yes or no isnt inputted then error message and exit
if Addition != 'yes' or 'no':
    print("Error")
    exit()
# Countdown to shut down
ShutDown =str(input ("Thanks For Using This Calculator, would you like the program to shut down, yes or no"))
if ShutDown == 'yes':
    print ("Goodbye")
    exit()
if ShutDown == 'no':
    def countdown(t):
        while t > 0:
            print(t)
            t -= 1
            time.sleep(1)
            print("PROGRAM SHUTTING DOWN IN: ")

print("How long do you need the calculator open for?")
seconds = input()
while not seconds.isdigit():
    print("That wasn't an integer! Enter an integer:")
    seconds = input()
seconds = int(seconds)
countdown(seconds)
exit()
