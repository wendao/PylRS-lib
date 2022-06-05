for i in A B C D E F G H
do
  python normalization_zscore.py fwd/U${i}_ddg_terms.txt 1 > train_U${i}_ddg_terms.txt
done

for i in X-ax X-ep
do
  python normalization_zscore.py ssm/U${i}_ddg_terms.txt 1 > ssm_U${i}_ddg_terms.txt
done
