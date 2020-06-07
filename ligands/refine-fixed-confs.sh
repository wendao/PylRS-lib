for d in UC-Kax UC-Kep UC-Yax UC-Yep
do
    cd $d
      echo $d
      python ../refine_rotamers.py fixed-confs.sdf
    cd ..
done
