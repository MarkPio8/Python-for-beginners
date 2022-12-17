def PrintCat():
    # this function prints a cat ascii-art
    txt = r'''
|\---/|
| o_o |
 \_^_/'''
    print(txt)
    return
 
def PrintBear():
    # this function prints a bear ascii-art
    txt = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    print(txt)
    return
 
def PrintBat():
    # this function prints a bat ascii-art
    txt = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''
    print(txt)
    return


def PrintAnimal(*animals):
    # this functiont prints took in animal
    for animal in animals:
        if animal == 'cat':
            PrintCat()
        elif animal == 'bear':
            PrintBear()
        elif animal == 'bat':
            PrintBat()
        else:
            print("Cannot print '%s'.Correct values for the parametere are: cat, bear, bat"%(animal))
        
    return 

PrintAnimal('cat','bear')




from datetime import date

def DaysToEndOfYear(*g):
    
    for dat in g:
        date_end_year = date(dat.year, 12, 31)
        delta = date_end_year - dat
        print(delta.days)


DaysToEndOfYear(date(2002,10,1),date(2001,12,30))







    
