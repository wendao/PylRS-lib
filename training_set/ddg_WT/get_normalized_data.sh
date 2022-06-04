#python normalization_zscore.py fwd/UA_ddg.txt test/UA_ddg.txt 0
for i in A B C D E F G H X-ax X-ep
do
  tail -n +2 fwd/U${i}_ddg_terms.txt > ref_U${i}.dat
  tail -n +2 test/U${i}_ddg_terms.txt >> ref_U${i}.dat
  python normalization_zscore.py ref_U${i}.dat ref_U${i}.dat > combined_U${i}_ddg_terms.txt
done

for i in X-ax X-ep
do
  tail -n +2 ssm/U${i}_ddg_terms.txt > ssm_U${i}.dat
  python normalization_zscore.py ref_U${i}.dat ssm_U${i}.dat > ssm_U${i}_ddg_terms.txt
done

