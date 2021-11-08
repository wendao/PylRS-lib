import sys
from collections import defaultdict
AA = [ "A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y" ]
lines = open("loc.txt", 'r').readlines()

#FMGGF
pre_muts = defaultdict(list)
pre_muts[305]= ["L","F"]
pre_muts[309]= ["L","M"]
pre_muts[346]= ["N","G"]
pre_muts[348]= ["C","G"]
pre_muts[384]= ["Y","F"]

i = 0
for l in lines:
    wt = l.strip()
    pos = int(wt[1:])
    wt = wt[0]
    pm = wt
    if pos in pre_muts.keys():
        pm = pre_muts[pos][1]
    #init
    for a in AA:
      if a != pm:
        i = i+1
        #single mutation
        #print( str(i)+","+wt+pos+a )
        #multi
        muts = pre_muts.copy()
        muts[pos] = [wt, a]
        print(str(i)+","+"|".join([muts[p][0]+str(p)+muts[p][1] for p in muts.keys()]))
