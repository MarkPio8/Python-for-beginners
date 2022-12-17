file_path = r'C:\Users\marek\OneDrive\Pulpit\pythonisko\python dla poczatkujacych\orders.csv'
import sys 
with open(file_path,"r") as file:
 
    for line in file:
    
        line = line.replace('\n','')
        order = line.split(',')
        
        try:
            pharmacyName = order[0]
            item = order[1]
            amount  = int(order[2])
            print('Order for drugstore "%s",item "%s", amount %d' % (pharmacyName,item,amount))

        except:
            print('Line which made error "%s"' %(line))
            print('Error information', sys.exc_info()[0])
 
print("Processing finished")
