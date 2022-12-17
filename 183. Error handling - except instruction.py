import sys
 
file_path = r'C:\Users\marek\OneDrive\Pulpit\pythonisko\python dla poczatkujacych\orders.csv'
 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' %
                      (pharmacy_name, item, amount))

        except ValueError as e:
            print('Line which made error: "%s"'% line)
            print(e)

        except IndexError as e:
            print('Line which made error: "%s"'% line)
            print(e)
            
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])
 
print("Processing finished")
