##1
number = 1
previousNumber = 0
while number <=50:
    print(number,'+',previousNumber,'=',number+previousNumber)
    number +=1
    previousNumber +=1

number = 1
previous_number = 0
 
##2

import random
myNumber = random.randint(0,20)
guess = -1
trials = 0
print('Guess my number!')

while myNumber != guess :
    guess = int(input())
    trials +=1
    if(guess == myNumber):
        print('Udalo Ci się ta liczba to',myNumber)
    elif(guess> myNumber):
        print('Liczba za duża')
    elif(guess< myNumber):
        print('Liczba za mala')

print('Liczba prób:',trials)
