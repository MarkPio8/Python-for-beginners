##1
initilaCapital = 20000
staticFirstCapital = initilaCapital
percent = 0.03
maxTimeYears = 10
i = 1
while(maxTimeYears >=1):
    maxTimeYears -=1
    initilaCapital += initilaCapital *percent   
    print('Po',i,'roku na koncie jest:',initilaCapital)
    i+=1
else:
    print('Po',maxTimeYears,'na koncie jest',initilaCapital,'co oznacza ze zarobiono:',initilaCapital-staticFirstCapital)


initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year=0
capital=initialCapital
while year<maxTimeYears:
    year+=1
    capital=round((1+percent)*capital,2)
    print('after this year:', year,  'you will have:',capital)
else:
    print('the total revenue is', capital-initialCapital)
print('-------------------------------------------------------')

print()
##2
print()

number = 20730906
temp = number
suma = 0
while(temp>0):

    suma += temp%10

    temp = temp//10

    
print(suma)

print()
##3
print()
text ='''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
textList = text.replace('\n',' ').replace('.',' ').replace(',',' ').replace('(',' ').split(' ')
shortWords = 0
longWords = 0
wordLength = 6

while(len(textList)>0): 
    if(len(textList[0])>wordLength):
        textList.pop(0)
        longWords +=1
    elif(len(textList[0])<=wordLength):
        textList.pop(0)
        shortWords +=1
    
print('Słow dluzszych od:',wordLength,'liczb jest:',longWords,'a krotszych jest:',shortWords)
    
    





text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
listOfWords = text.replace('\n',' ').split(' ')
wordLength = 6
i=0
shortWords = 0
longWords = 0
while i< len(listOfWords):
    if len(listOfWords[i])>wordLength:
        longWords+=1
    else:
        shortWords+=1
    
    i+=1
print("Words shorter than ",wordLength,":",shortWords)
print("Words longer than ",wordLength,":",longWords)




