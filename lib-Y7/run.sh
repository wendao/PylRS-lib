for i in X-ax X-ep A B C D E F G H
do
cd U${i}
#mv ../opt${i}.inp .
#/home/wendao/install/orca_5_0_1_linux_x86-64_shared_openmpi411/orca opt${i}.inp > opt.out
#orca_2mkl opt${i} -molden

/home/wendao/install/orca_5_0_1_linux_x86-64_shared_openmpi411/orca opt${i}-gas.inp > opt-gas.out
/home/wendao/install/orca_5_0_1_linux_x86-64_shared_openmpi411/orca opt${i}-wat.inp > opt-wat.out
orca_2mkl opt${i}-gas -molden
orca_2mkl opt${i}-wat -molden
cd ..
done

