#1
musclePain = False
fever = False
weakness = True

#2
if musclePain and fever and weakness:
    print('suspicion of influenza')
else:
    print('the flu is unlikely')

#3
if musclePain and fever and weakness:
    print('suspicion of influenza')
elif weakness and not fever and not musclePain:
    print('Just take a rest!')
else:
    print('You may be cold')

#4
isMan = True

#5
if (musclePain and fever and weakness) or (isMan and(musclePain or fever or weakness)):
    print('suspicion of influenza')
elif weakness and not fever and not musclePain:
    print('Just take a rest!')
else:
    print('You may be cold')



#6
isCheckCompleted = True
print('CHECK IS COMPLETED'if isCheckCompleted else 'Check not done yet!')





























