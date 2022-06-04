for i in X-ax X-ep
do
cd U${i}
python ../../WT_to_muts/parse_newdata_ddg.py > results.txt
python ../../WT_to_muts/parse_newdata_ddg_terms.py > results-terms.txt
cp results.txt /home/wendao/work/PylRS/PylRS-lib/training_set/ddg_WT/ssm/U${i}_ddg.txt
cp results-terms.txt /home/wendao/work/PylRS/PylRS-lib/training_set/ddg_WT/ssm/U${i}_ddg_terms.txt
cd ..
done
