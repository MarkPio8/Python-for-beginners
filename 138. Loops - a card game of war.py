colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []

for color in colors:
    for figure in figures:
        aCard = figure.copy()
        aCard = (aCard , color)
        allCards.append(aCard)

import random

random.shuffle(allCards)
print('-----------------')
print(allCards)
print('-----------------')

numberOfPlayers = 2
halfCards = int((len(allCards))/numberOfPlayers)

player1 = allCards[:halfCards]
player2 = allCards[halfCards:]
print('-----------------')
print(player1)
print('-----------------')
print(player2)
print('-----------------')


while len(player1)>0 and len(player2)>0:
    
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    print('Player 1 played card:', card1)
    print('Player 2 played card:', card2)
    
    if card1[0]['Power'] == card2[0]['Power']:
        player1.append(card1)
        player2.append(card2)
        print('remis')
        
    elif card1[0]['Power'] > card2[0]['Power']:
        player1.append(card1)
        player1.append(card2)
        print('Won first player now have:',len(player1),'cards')

    elif card1[0]['Power'] < card2[0]['Power']:
        player2.append(card1)
        player2.append(card2)
        print('Won second player now have:',len(player2),'cards')

else:
    if(len(player1)==0):
        print('Player2 won')
    else:
        print('Player1  won')
