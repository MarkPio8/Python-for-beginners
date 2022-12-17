##1
a=0
b=1
c=0
fibonacciIterations = 20
print(a)
print(b)
a+=1
for i in range(2,fibonacciIterations-1):
    
    c = a + b
    a = b
    b = c


    print(c)
print()
##2
print()
text = '''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
'''

listOfWord = text.lower().replace('\n',' ').split(' ')


for word in listOfWord:
   
    if(word.find('p')>=0):
       print(word)

print()
##3
print()

dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less than 50%'}


for word in dictionary.keys():
    print(word,'-',dictionary[word])



print()
##4
print()
text = '''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
'''
wordDictionary = {}

listOfWords = text.lower().replace('\n',' ').split(' ')

print(a)
for word in listOfWords:
    #jak przeszukac disciotnary,kyes
    if(list(wordDictionary.keys()).count(word)>0):
        wordDictionary[word]+=1
    else:
        wordDictionary.setdefault(word,1)

print(wordDictionary)
























