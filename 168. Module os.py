import os,time

dir = input('Enter dir:')

if not os.path.exists(dir):
    print('wrong dir')
    
else:
    file = input('File name:')

    path  = os.path.join(dir,file)

    if not os.path.exists(path):
        print('this file does not exist')
        
    else:
        print('Date of last modification:',time.localtime(os.path.getmtime(path)))
        print('Size of file (mb):',os.path.getsize(path))
        print('Absoluth path:',os.path.abspath(path))
        print('Current director is:',os.getcwd())
        print('Rel path:',os.path.relpath(path))
