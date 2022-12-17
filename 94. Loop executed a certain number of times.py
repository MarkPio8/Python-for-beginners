string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'


for i in range(20):
    print(string_A)

print()
print('XXXXXXXXXXXXXXXXXXXXXX')
print()

for i in range(20):
    if i%2 ==0:
        print(string_A)
    else:
        print(string_B)

print()
print('XXXXXXXXXXXXXXXXXXXXXX')
print()

for i in range(1,20):
    print('x'*i)


print()
print('XXXXXXXXXXXXXXXXXXXXXX')
print()

for i in range(1,20):
    if i%2==0:
        print('x'*i)
    else:
        print('o'*i)
