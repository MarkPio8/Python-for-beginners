##1 

like = 5000
share = 555

minLikes = 500
minShares = 100

if like>=minLikes and share>=minShares:
    print('Żnizka 10 %')
else:
    print('jeszcze brakuje')

##2

isPizzaOrdered = True
isBigDrinkOrdered = False
isWeekend = False

if (isPizzaOrdered or isBigDrinkOrdered) and not isWeekend:
    print('Zostaje przyznany kupon')

else:
    print('Brak kupon')

##3
diskSize = 222
diskSizeUsed = 133
fileSize = 10
if diskSize-diskSizeUsed>fileSize:
    print('Enough space')
else:
    print('Za malo miejsca')









    
