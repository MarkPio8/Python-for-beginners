#zad 2
q = 'THE EYES'
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])

#zad 3
q = 'a gentleman'
print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])

#zad 4
q = "THE MORSE CODE"
print(q[1:3]+q[6]+q[8],q[10:12]+q[4]+q[2],q[12]+q[11]+q[0]+q[7])

#zad 5
line =  'Program "Kropka nad i" nadamy o: 22:00'
print(line)

time = line[line.find(":")+2:]
print(time)

tmp = line[line.find('"')+1:]
print(tmp)
title = tmp[:tmp.find('"')]
print(title,time)

line =  'Program "Pytanie na śniadanie" nadamy o: 6:00'
print(line)

time = line[line.find(":")+2:]
print(time)

tmp = line[line.find('"')+1:]
print(tmp)
title = tmp[:tmp.find('"')]
print(title,time)
