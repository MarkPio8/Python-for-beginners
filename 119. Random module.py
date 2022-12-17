#1
import random
#2
for i in range(0,9):
    i+=1
    print(random.randint(1,100))

#3
number1 = random.randint(1,100)
print('wylosowana liczba to', number1)
counter = 1
number2 = random.randint(1,100)
while number1!=number2:
    counter +=1 
    number2 = random.randint(1,100)
    #print('Próba:',counter,'wylosowanao:', number2)
else:
    print('Udało się wylosować tą samą liczbę: ',number1,'ilość prób:',counter)

#4
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
random.shuffle(countries)
groupNumber = 0
for i in range(0,len(countries)):
    if(i%4==0):
        groupNumber += 1
        print('-----Grupa',groupNumber,'------')
    print(countries[i])






















    
    
