for i in $(cat list)
do 
	python ../1_extract_homo.py $i homo.$i
	python ../2_homo_break.py homo.$i bk.$i
	python ../3_extract_homo_snp.py $i bk.$i hmsnp.$i
	rm homo.$i bk.$i
	python ../4_snp_fil.py hmsnp.$i heter.hmsnp.$i filter.hmsnp.$i
done

cat heter.hmsnp.* | awk '{print$3}' | sort -u -n > heter-snp-ch01.txt
#rm heter.hmsnp.*
mkdir ch01-A ch01-B ch01-raw
