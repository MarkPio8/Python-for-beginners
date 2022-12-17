import os

webAddresses = []
line =  input('Enter web address like "www.python.org" or press ENTER to stop: ')
    
while line:
    webAddresses.append(line)
    line = []
    line = input('Enter next web addres or press ENTER: ')
    


dirname = os.getcwd()

filename = input('Enter filename: ')

filepath = os.path.join(dirname,filename)

with open(filepath,mode = 'w+') as file:
    
    for addres in webAddresses:
        file.write(addres+'\n')
        
