for d in UA-K UA-Y UB-K UB-Kax UB-Kep UB-Y UB-Yax UB-Yep UC-Kax UC-Kep UC-Yax UC-Yep
do
    cd $d
    #mkdir rotlib
    cd rotlib
      #../../gen_pml_rot2.sh > gen_rotamers.pml
      #pymol gen_rotamers.pml
      #acpype.py -i lig.mol2 -n -1

      cp lig.acpype/lig_bcc_gaff.mol2 .
      convert_qm2mol2.sh lig_bcc_gaff.mol2

      root=$(grep 'N.2' lig_bcc_gaff.mol2 | awk '{print $1}')
      /home/wendao/bakerlab/Rosetta/main/source/scripts/python/public/molfile_to_params.py lig_bcc_gaff.mol2 -n LIG --root_atom=$root --extra_torsion_output --clobber

      python ../../gen_rot_lib.py LIG_0001.pdb ROT_0*pdb > rotlib.pdb
      cp LIG.params LIG0.params
      echo "PDB_ROTAMERS rotlib.pdb" >> LIG.params
    cd ..
    cd ..
done
