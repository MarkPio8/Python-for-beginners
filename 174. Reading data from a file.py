filePath = 'C:\\temp\\data_input\\orders.csv'


with open(filePath, mode ='r') as file:
    for line in file:
        
        line = line.replace('\n','')
        order  = line.split(',')
        
        if len(order) == 3:
            print('Order form drugstore "%s",item "%s", amoutn %s' % (order[0],order[1],order[2]))

        else:
            print('Line %s malformed!!!' % (line))
            
    print('Processing finished')
