age = 19
isDrunk = True
isRestrictedArea = True


if age < 18:
    print('You are too young to buy alcohol')
else:
    if isDrunk:
        print('Are you drunk? We cannot sell you alcohol')
    else:
        if isRestrictedArea:
            print('Restricted area. Alchochol is forbiedden')
        else:
            print('OK, you can buy alcochol')

print("======")



if age <18:
    print('You are too young to buy alcochol')
elif isDrunk:
    print('Are you drunk? We cannot sell you alcohol')
elif isRestrictedArea:
    print('Restricted area. Alchochol is forbiedden')
else:
    print('Ok,you can buy alcochol')
