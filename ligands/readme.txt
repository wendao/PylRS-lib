#gen confs

#confs.sdf -> mol2
../gen_pml.sh confs > gen_rotamers.pml
pymol gen_rotamers.pml 
mkdir raw
mv ROT*mol2 raw/

#fit TCO
mkdir fit
../fit_TCO.sh ax > aln.pml
pymol aln.pml

#assign and convert
../replace_TCO.sh > convert.pml
pymol convert.pml

#combine
python ../fix_TCO.py 

mkdir rotlib
cd rotlib
../../gen_pml_rot.sh > gen_rotamers.pml
pymol gen_rotamers.pml
