def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

print('Podaj wspólcznynniki funkcji w kolejnosc a b c')

a = input('a =')
b = input('b =')
c = input('c =')

while True:
    if check_int(a) != True :
        print(a,'to nie jest liczba wprowadz ponownie')
        a = input('a =')
        
    elif check_int(b) != True :
        print(b,'to nie jest liczba wprowadz ponownie')
        b = input('b =')
        
    elif check_int(c) != True :
        print(c,'to nie jest liczba wprowadz ponownie')
        c = input('c =')
        
    else:
        print('wszystkie liczby wprowadzono poprwanie')

        a = int(a)
        b = int(b)
        c = int(c)

        if a == 0:
            print('to nie jest rownanie kwadratowe')
            break
        
        else:
            delta = b**2-4*a*c

            if delta > 0:
               deltaSqrt = delta ** (1/2)
               x1 = ((-1*b)-deltaSqrt)/(2*a)
               x2 = ((-1*b)+deltaSqrt)/(2*a)
               print('Dwa miejsca zerowe:',x1,x2)
               break
                
            elif delta ==0:
               deltaSqrt = delta ** (1/2)
               x1 = ((-1*b)-deltaSqrt)/(2*a)
               print('Jedno miejsce zerowe:',x1)
               break
                
            elif delta < 0:
                print('Brak miejsc zerowych')
                break
                
        

