##1

minLike = 500
minShare = 100
like = 100
share = 5


if like >=minLike and share >= minShare:
    print('Promocja')
else:
    if like >= minLike and share<minShare:
        print('Za mało udostępnien')
    else:
        if like< minLike and share>= minShare:
            print('Za mało likow')
        else:
            print('Za malo like i za malo share')





if like >=minLike and share >= minShare:
    print('Promocja')
elif like >= minLike and share<minShare:
    print('Za mało udostępnien')
elif like< minLike and share>= minShare:
    print('Za mało likow')
else:
    print('Za malo like i za malo share')
    

print()
print()
print()

#2
isPizzaOrdered = True
isWeekend = False
isBigDrink = True


if (isPizzaOrdered or isBigDrink) and not isWeekend:
    print('Dostajesz kupon')
elif(isPizzaOrdered or isBigDrink) and isWeekend:
    print('Nie ma kupona tylko w dni robocze')
elif not(isPizzaOrdered or isBigDrink) and not isWeekend:
    print('Nie ma kupona nie zamowiles pizza lub duzego napoju')
    








































