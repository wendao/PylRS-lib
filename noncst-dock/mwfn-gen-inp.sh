for i in $(seq 200 | awk '{printf("%04d\n",$1)}')
do
echo LIG_${i}.out $(grep pure ../complex_${i}.pdb | awk '{print $2}') $(grep 'FINAL SINGLE POINT ENERGY' LIG_${i}.out | awk '{print $5}')
#  Multiwfn << __EOF__
#LIG_${i}.pdb
#100
#2
#12
#
#1
#0
#q
#__EOF__
#perl -pi -e "s/xyz   0/xyz   -1/" LIG_${i}.inp
#/home/wendao/install/orca_5_0_1_linux_x86-64_shared_openmpi411/orca LIG_${i}.inp > LIG_${i}.out
done
