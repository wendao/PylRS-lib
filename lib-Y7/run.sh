#for ORCA
#export PATH=/home/wendao/install/orca_5_0_1_linux_x86-64_shared_openmpi411:$PATH
#export LD_LIBRARY_PATH=/home/wendao/install/orca_5_0_1_linux_x86-64_shared_openmpi411:$LD_LIBRARY_PATH
#export PATH=/opt/omp411/bin:$PATH
#export LD_LIBRARY_PATH=/opt/omp411/lib:$LD_LIBRARY_PATH

#for Multiwfn setup
#export KMP_STACKSIZE=200M
#ulimit -s unlimited

for i in X-ax X-ep A B C D E F G H
do
echo $i
cd U${i}
## OPT
#mv ../opt${i}.inp .
#/home/wendao/install/orca_5_0_1_linux_x86-64_shared_openmpi411/orca opt${i}.inp > opt.out
#orca_2mkl opt${i} -molden

## gen input
## charge 0 2 -> -1 1
#~/source/Multiwfn_3.8_dev_bin_Linux/Multiwfn << __EOF__
#opt${i}.xyz
#100
#2
#12
#opt${i}-gas.inp
#5
#2
#12
#opt${i}-wat.inp
#-1
#water
#5
#0
#0
#q
#__EOF__

## SP
#/home/wendao/install/orca_5_0_1_linux_x86-64_shared_openmpi411/orca opt${i}-gas.inp > opt-gas.out
#/home/wendao/install/orca_5_0_1_linux_x86-64_shared_openmpi411/orca opt${i}-wat.inp > opt-wat.out
#orca_2mkl opt${i}-gas -molden
#orca_2mkl opt${i}-wat -molden

## charge
#~/source/Multiwfn_3.8_dev_bin_Linux/Multiwfn << __EOF__
#opt${i}-gas.molden.input
#7
#18
#1
#y
#0
#0
#q
#__EOF__
#
#~/source/Multiwfn_3.8_dev_bin_Linux/Multiwfn << __EOF__
#opt${i}-wat.molden.input
#7
#18
#1
#y
#0
#0
#q
#__EOF__

## average charge
python ../map_resp_charge.py LIG_0001.pdb opt${i}-gas.molden.chg opt${i}-wat.molden.chg LIG.params > LIG1.params
cd ..
done

