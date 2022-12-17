import random
min = 1
max = 6

dice = random.randint(min,max)
print(dice)

if dice == 1:
    print('''   
 o 
   
 ''')
elif dice == 2:
    print('''
  o
   
o  
 ''')
elif dice == 3:
    print('''
  o
 o 
o  
 ''')
elif dice == 4:
    print('''
o o
   
o o
 ''')
elif dice == 5:
    print('''
o o
 o 
o o
''')
elif dice == 6:
    print('''
o o
o o
o o
''')


dices = []

for i in range(0,5):
    dices.append(random.randint(min,max))
print(dices)















    
