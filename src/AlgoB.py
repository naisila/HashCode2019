#!/usr/bin/env python

"""AlgoB.py: Optimized algorithm for B input"""

__author__      = "Naisila Puka, Fatbardh Feta"

f = open("b_lovely_landscapes.txt", "r")
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
    for j in range (3, len( ptemp[ i])):
        if ptemp[i][j] in dicti:
            dicti[ptemp[i][j]].append(i-1)
        else:
           dicti[ptemp[i][j]] = [i-1]

listi = []
dictio = {}
for key, value in dicti.items():
    for i in value:
        if i not in dictio:
        #if i not in listi:
            listi.append(i)
            dictio[i] = 1

print(len(listi))
for i in listi:
    print(str(i))