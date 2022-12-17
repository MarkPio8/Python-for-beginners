import os,sys


line = input('How much can you pay for next course: ')

path = input('Enter path to file where you want to save answers:')

try:
    file = open(path,'w+')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is %d' % value)

except FileNotFoundError as e:
    print('Error opening file',e)

except ValueError as e:
    print('The value entered cannot be converted to a number',e)

except:
    print('SORRY WE HAVE AN ERROR. PLEASE TRY AGAIN',sys.exc_info()[0])

else:
    print('Action completed successfully')
