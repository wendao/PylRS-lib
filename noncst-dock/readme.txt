plot [:][:-68.5] "UX-ax/lig-X-ax/all.results.txt" u 2:($3+2122)*100 w p pt 6, "UX-ep/lig-X-ep/all.results.txt" u 2:($3+2122)*100 w p pt 6
awk '$3<-2122.688{print $1, $2, $3}' all.results.txt | sort -nrk2

/lustre1/chuwang_pkuhpc/rosetta/rosetta_src_2019.47.61047_bundle/main/source/bin/rosetta_scripts.mpi.linuxiccrelease -s complex.pdb -parser:protocol ../refine.xml -score:weights ref2015 -nstruct 10 -ex1 -ex2 -use_input_sc -flip_HNQ -no_optH false -extra_res_fa LIG.params
