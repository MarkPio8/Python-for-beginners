import os, datetime

dataInputCatalog = 'c:\\temp\\data_input'
dataOutputCatalog = 'c:\\temp\\data_output'

today = datetime.date.today()

todayOutputCatalog = dataOutputCatalog + today.strftime('%Y-%m-%d')                                           

print(todayOutputCatalog)

isInputCatalogOk = os.path.isdir(dataInputCatalog)
isOutputCatalogOk = os.path.isdir(dataOutputCatalog)
isTodayOutpotCatalogOK = not os.path.isdir(todayOutputCatalog) and not os.path.isfile(todayOutputCatalog)

if isInputCatalogOk and isOutputCatalogOk and isTodayOutpotCatalogOK:
    print('Conditions met! We can continue!')
else:
    print('Error!')
    if not isInputCatalogOk:
        print('%s input catalog dont exists'%dataInputCatalog)
    elif not isOutputCatalogOk:
        print('%s output catalog dont exists'%dataOutputCatalog)
    elif not isTodayOutpotCatalogOK:
        print("%s today 's output cannot exists (neiter as file as directory)"%todayOutputCatalog)
 
