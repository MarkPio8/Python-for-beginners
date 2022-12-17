##1
import math
##2,3,4
degree = 45
rad = (degree*(2*math.pi))/360
print(rad)
##5
print(math.radians(45))
##6 price and radius
smallPizzaR = 0.22
smallPizzaPrice = 11.50

bigPizzaR = 0.27
bigPizzaPrice = 15.60

familyPizzaR = 0.38
familyPizzaPrice = 22.00

##7 surface area
smallSurfaceArea = math.pi * math.pow(smallPizzaR,2)
print(smallSurfaceArea)

bigSurfaceArea =  math.pi * math.pow(bigPizzaR,2)
print(bigSurfaceArea)

familySurfaceArea  = math.pi * math.pow(familyPizzaR,2)
print(familySurfaceArea)

##8 price per square meter

smallSquareMeter = smallPizzaPrice/ smallSurfaceArea   

bigSquareMeter = bigPizzaPrice/ bigSurfaceArea   

familySquareMeter =  familyPizzaPrice/familySurfaceArea  
print(smallSquareMeter, bigSquareMeter, familySquareMeter)


math_ls = dir(math) 
print(math_ls)

