import math

def GiveGeomSeqElement(a1 = 2,factor = 2, index = 2):
    #this function returns given number of geometric sequent element
    an =  math.pow(factor,index-1)*a1
    return(an)

def GiveFactorForGeomSeq(a1,a2):
    #this function return factor of 2 next to each other number in geometric sequent
    factor = a2/a1
    return factor

def GiveSumOfNElementsGeomSeq(a1 = 2, factor = 2, n = 2):
    #this function return sum a geometric sqeuent
    suma = (a1*(1-(factor**n)))/(1-factor)
    return suma
