##1
i = 10
sum = 1

for a in range(1,i+1):
    sum = sum * a
print(sum)

print()
##2
print()

i = 10
sum = 1

for a in range(1,i+1):
    sum=1
    for b in range(1,a+1):
        sum = sum * b

    print('Silnia dla liczby',b,'=',sum) 
    
print()
##3
print()

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']  

for a in list_noun:
    for b in list_adj:
        print(b,a)
