import os
filename = input('Enter file path')
filename = 'C:\\Users\\marek\\OneDrive\\Pulpit\\pythonisko\\python dla poczatkujacych\\kot'
while True:
    if os.path.isfile(filename):
        print('Great path')
        break
    else:
        filename = input('Wrong path enter again: ')

webadresses  = []

file = open(filename,'r')

for line in file:
    line = line.replace('\n','')
    webadresses.append(line)

websPlFilePath = os.path.join(os.path.dirname(filename),'webs_pl.txt')
websOtherFilepath = os.path.join(os.path.dirname(filename),'webs_other.txt')

plFile = open(websPlFilePath,'w')
otherFile = open(websOtherFilepath,'w')


for adress in webadresses:
    if adress.endswith('.pl'):
        print('%s it is Poland adress'% adress)
        plFile.write(adress+'\n')
    else:
        print('%s it is not Poland adress'% adress)
        otherFile.write(adress+'\n')
    


file.close()
plFile.close()
otherFile.close()
