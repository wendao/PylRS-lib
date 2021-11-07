import sys
AA = [ "A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y" ]
lines = open("loc.txt", 'r').readlines()
i = 0
for l in lines:
    wt = l.strip()
    pos = wt[1:]
    wt = wt[0]
    for a in AA:
      if a != wt:
        i = i+1
        print( str(i)+","+wt+pos+a )
