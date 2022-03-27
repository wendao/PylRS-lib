import sys
import numpy as np
from collections import defaultdict

fn2tag = defaultdict(list)
lines = open("map_label_fname.txt", 'r').readlines()
for l in lines:
    es = l.strip().split()
    tag = es[0]
    fn = es[1]
    fn2tag[fn].append(tag)

lines = open(sys.argv[1],'r').readlines()
results = defaultdict(list)
for l in lines:
    es = l.split()
    fn = es[0][:-16]
    tags = fn2tag[fn]
    rep = []
    for sc in es[1:]:
        rep.append(float(sc))
    for tag in tags:
        results[tag].append(rep)

np.set_printoptions(linewidth=np.inf)
np.set_printoptions(precision=4)
for tag in results.keys():
    reps = np.array(results[tag])
    ave = np.mean(reps, axis=0)
    astr = np.array2string(ave, precision=4, separator=',')
    print(tag+","+astr[1:-1])

## uniq tag
for tags in fn2tag.values():
    if len(tags)>1:
        print tags
