import sys
import numpy as np
from collections import defaultdict

max_zscore = 5

nskip = int(sys.argv[-1])
data = defaultdict(lambda: defaultdict(float))
for fn in sys.argv[1:-1]:
    lines = open(fn, 'r').readlines()
    for l in lines[nskip:]:
        es = l.strip().split()
        for i, e in enumerate(es[1:]):
            data[i][es[0]]=float(e)
Ndat = len(data.keys())
#fill in B1
for i in range(Ndat):
    data[i]['B1'] = 0.0

mu = defaultdict(float)
sigma = defaultdict(float)
for k in data.keys():
    x_raw = np.array(data[k].values())
    tmp_mu = np.mean(x_raw)
    x0 = x_raw - tmp_mu
    tmp_sigma = np.std(x0)
    if tmp_sigma < 1e-6:
        #print "skip", k
        continue
    mu[k] = tmp_mu
    sigma[k] = tmp_sigma

#1. raw
#2. mean 0
#3. mean 0, zscore
for mut in data.values()[0].keys():
    out_str = mut
    for k in mu.keys():
        #z = (data[k][mut]-mu[k])/sigma[k]
        #if z > max_zscore: z = max_zscore
        #elif z < -max_zscore: z = -max_zscore
        out_str += "\t%4.2f" % data[k][mut]
    print out_str
