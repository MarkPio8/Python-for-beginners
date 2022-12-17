#1
chanels = {'Google':1480,'Email':300,'Natural Traffic':400,'TV Sport':700}
print("1.",chanels)

#2
print('2.',chanels['Email'])

#3
chanelsUpdate = {'Natural Traffic':520,'News':600}
print('3.',chanelsUpdate)

#4
chanels.update(chanelsUpdate)
print('4.',chanels)

#5
print('5.',chanels.keys())

#6
print('6.',chanels.pop('Email'))
print('6.',chanels)
