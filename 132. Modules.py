inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
print()
##1
print()
import math

print(len(inputdata))
print(len(factortable))

if(len(inputdata)==len(factortable)):

    for i in range(0,len(inputdata)-1):
        minValue = inputdata[i] - factortable[i] * inputdata[i]
        maxValue = inputdata[i] + factortable[i] * inputdata[i]
        print('minvalue =',minValue,'maxvalue =',maxValue)
        
        minInteger = math.floor(minValue)
        maxInteger = math.ceil(maxValue)
        print('min Integer=',minInteger,'n-ty element list inputa =',inputdata[i],'max integer',maxInteger)  
        
else:
    print('inputdata and factortable need to have equal number of elements')
    
print()
##2
print()
import random
for i in range(0,len(inputdata)-1):
    minValue = inputdata[i] - random.random() * inputdata[i]
    maxValue = inputdata[i] + random.random() * inputdata[i]
    print('minvalue =',minValue,'maxvalue =',maxValue)
    
    minInteger = math.floor(minValue)
    maxInteger = math.ceil(maxValue)
    print('min Integer=',minInteger,'n-ty element list inputa =',inputdata[i],'max integer',maxInteger) 

print()
##3
print()

import datetime
print(datetime.datetime.today())
print(datetime.datetime.now().strftime('%Y-%m-%d'))














