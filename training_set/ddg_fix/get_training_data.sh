for i in A B C D E F G H X-ax X-ep
do
  tail -n +2 fwd/U${i}_ddg_terms.txt > tmp_U${i}.dat
  python normalization_zscore.py tmp_U${i}.dat tmp_U${i}.dat > train_U${i}_ddg_terms.txt
done

for i in X-ax X-ep
do
  tail -n +2 ssm/U${i}_ddg_terms.txt > test_U${i}.dat
  python normalization_zscore.py tmp_U${i}.dat test_U${i}.dat > test_U${i}_ddg_terms.txt
done

