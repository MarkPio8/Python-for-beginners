helloMessage = 'Hello %s!'
print(helloMessage %('Kate'))
print(helloMessage % ('Chirs'))
helloMessage = 'Hello {0:s}!'
print(helloMessage.format('Kate'))
print(helloMessage.format('Chirs'))
helloMessage = '%s has %d %s'
print(helloMessage % ('Kate',1,'animal'))
print(helloMessage % ('Chris',1000000,'$'))
#7
helloMessage = '{0:s} has {1:d} {2:s}'
print(helloMessage.format('Kate',1,'animal'))
print(helloMessage.format('Chris',1000000,'$'))
#9
line = '{0:20s} costs {1:6d}€'
print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAI',6))
