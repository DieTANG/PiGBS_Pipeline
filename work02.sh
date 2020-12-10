for i in `ls filter.hmsnp.*`
do
	python 5_cmp_and_move.py filter.hmsnp.RH-001-ch01 $i >> cmp.txt
done
### split homo region and move to GroupA GroupB ###
for i in `ls filter.hmsnp.*`
do
	awk '{print $1}' $i | uniq > split_id
	python ../6_split_and_move.py $i filter.hmsnp.RH-001-ch01 >> cmp_2.txt
done
#rm filter.hmsnp.RH-001*_homo* 
mv filter.hmsnp.* ch01-raw/
### Group A
cd ch01-A/
cat filter.* | awk '{print$3}' | sort -u -n > ch01-A_pos.txt
for i in `ls filter.hmsnp.*`
do
	python ../../7_haplotype_raw.py $i ch01-A_pos.txt $i.out
done
paste ch01-A_pos.txt filter.*.out > ch01-A_all-snp.txt
python ../8_haplotype_com.py ch01-A_all-snp.txt ch01-A_geno_raw.txt
rm filter.*.out
mv ch01-A_geno_raw.txt ../
### Group B
cd ../ch01-B/
cat filter.* | awk '{print$3}' | sort -u -n > ch01-B_pos.txt
for i in `ls filter.hmsnp.*`
do
	python ../../7_haplotype_raw.py $i ch01-B_pos.txt $i.out
done
paste ch01-B_pos.txt filter.*.out > ch01-B_all-snp.txt 
python ../8_haplotype_com.py ch01-B_all-snp.txt ch01-B_geno_raw.txt 
rm filter.*.out 
### Generate ch01-B_geno.txt
mv ch01-B_geno_raw.txt ../
cd ../
python ../9_haplotype_com_A_B.py heter-snp-ch01.txt ch01-A_geno_raw.txt ch01-B_geno_raw.txt ch01-A-B_geno.txt
awk '{print$1,$2,$4}' ch01-A-B_geno.txt > ch01-B_geno.txt
