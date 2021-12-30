for i in X-ax X-ep A B C D E F G H
do
cd U${i}
cat ../B1-af2.pdb ../../lib-Y7/U${i}/LIG_0001.pdb | grep -v END > complex.pdb
cp ../../lib-Y7/UA/LIG.params .
cp ../../lib-Y7/UA/rotlib.pdb .
cd ..
done
