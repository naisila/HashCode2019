#!/usr/bin/env python

"""AlgoD.py: Optimized algorithm for D input"""

__author__      = "Naisila Puka, Fatbardh Feta"

f = open("d_pet_pictures.txt", "r")
photos = []
for i in f:
    photos.append(i)

ptemp = list(photos)

j=-1
for i in ptemp:
    ptemp[j +1 ] = str(j)+" "+ i
    ptemp[j +1 ] = ptemp[j +1].split()
    j = j + 1

dicti = {}



for i in  range(1, (int)(ptemp[0][1]) + 1):
    if (ptemp[i][1] == 'V'):
    	continue
    for j in range (3, len( ptemp[ i])):
        if ptemp[i][j] in dicti:
            dicti[ptemp[i][j]].append(i-1)
        else:
           dicti[ptemp[i][j]] = [i-1]

listi = []
for key, value in dicti.items():
	for i in value:
		if i not in listi:
			listi.append(i)

#print(listi)
dictio = {}
print(len(listi))
for i in listi:
		
	if i not in dictio:
		
		print(str(i))
		dictio[i] = 1
