for d in UA-K UA-Y UB-K UB-Kax UB-Kep UB-Y UB-Yax UB-Yep
do
    cd $d
      echo $d
      python ../refine_rotamers.py confs.sdf
    cd ..
done
