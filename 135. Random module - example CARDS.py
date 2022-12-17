##1

colors = ['Hearts','Diamonds','Clubs','Spades']

figures = ['Ace','King','Queen','Jack','10','9']

##2

allCards = []

##3

for color in colors:
    for figur in figures:
        allCards.append(color+' '+figur)

##4
        
print(allCards)

##5

import random

##6

random.shuffle(allCards)
print(allCards)

##7

player1 = []
player2 = []

##8

max = len(allCards)

for i in range(0,max-1):
    if i%2==0:
        player1.append(allCards[i])
    elif i%2!=0:
        player2.append(allCards[i])
print('----------')
print(player1)
print(player2)
print('----------')

##9
player1=(allCards[:12])
player2=(allCards[12:])
print('----------')
print(player1)
print(player2)
print('----------')
