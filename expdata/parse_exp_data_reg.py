import sys
import pandas as pd
import numpy as np

data = pd.read_csv(sys.argv[1], sep=',', header=None)

ligands = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' ]
N_lig = len(ligands)
N_pos = 96
cutoff = 2.5

pn = {}
for i in range(12):
  pn[i+1]    = "A"+str(i+1) #= "I"+str(i+1) #
  pn[i+1+12] = "B"+str(i+1) #= "J"+str(i+1) #
  pn[i+1+24] = "C"+str(i+1) #= "K"+str(i+1) #
  pn[i+1+36] = "D"+str(i+1) #= "L"+str(i+1) #
  pn[i+1+48] = "E"+str(i+1) #= "M"+str(i+1) #
  pn[i+1+60] = "F"+str(i+1) #= "N"+str(i+1) #
  pn[i+1+72] = "G"+str(i+1) #= "P"+str(i+1) #
  pn[i+1+84] = "H"+str(i+1) #= "Q"+str(i+1) #
#print pn

for i in range(N_lig):
  ns = i*6
  pos1 = data.loc[ns][1:]
  neg1 = data.loc[ns+1][1:]
  bg1 = (np.median(pos1) + np.median(neg1))/2.0
  pos2 = data.loc[ns+2][1:]
  neg2 = data.loc[ns+3][1:]
  bg2 = (np.median(pos2) + np.median(neg2))/2.0
  pos3 = data.loc[ns+4][1:]
  neg3 = data.loc[ns+5][1:]
  bg3 = (np.median(pos3) + np.median(neg3))/2.0
  bg_mean = np.mean([bg1, bg2, bg3])
  out_str = ""
  for j in range(N_pos):
    pos = []
    neg = []
    pos.append(pos1[j+1])
    pos.append(pos2[j+1])
    pos.append(pos3[j+1])
    neg.append(neg1[j+1])
    neg.append(neg2[j+1])
    neg.append(neg3[j+1])
    pos_mean = np.mean(pos)
    neg_mean = np.mean(neg)
    fold = pos_mean / ( neg_mean + bg_mean )
    print ligands[i], pn[j+1], fold
