import math
import geom

geom.GiveGeomSeqElement(1,3,4)

a1 = 3
factor = 2
index =10
for i in range(1,index+1):
    an = geom.GiveGeomSeqElement(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)

print(geom.GiveFactorForGeomSeq(12,24))

print(geom.GiveSumOfNElementsGeomSeq(2,3,4))
