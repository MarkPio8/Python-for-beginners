#1
hitsTitles = ['BROTHERS IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']

#2
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
##hitsTitles +=['CHILD IN TIME','AGAIN']

#3
hitsTitles.insert(2,'HOTEL CALIFORNIA')

#4
hitsTitles.insert(0,'THE SOUND OF SILENCE')

#5
print(hitsTitles.index('HOTEL CALIFORNIA'))

#6
hitsTitles.remove(hitsTitles[hitsTitles.index('HOTEL CALIFORNIA')])

#7
hitsTitles[0]='ENJOY THE SILENCE'

#8
hitsToRead = hitsTitles.copy()

#9
hitsToRead.reverse()

#10
hitsToRead.sort()

#11
print(hitsToRead.pop(0))
print(hitsToRead.pop(0))

#12
additionalSongs  = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE']

#13
hitsToRead.extend(additionalSongs)

#14
print(hitsToRead.count('WISH YOU WERE HERE'))
print(hitsToRead.count('RIDERS ON THE STORM'))
#15
hitsToRead.clear()

print(hitsToRead)
print(hitsTitles)
