#!/bin/bash

for i in $(cat list)
do
	python ../10_snp_geno.py ch01-B_geno.txt $i geno-$i
	python ../11_bin_snp_num_w200.py geno-$i w200-$i
	python ../12_bin_pos.py w200-$i bk-$i
done

cat bk-RH-001-* | sort -n -u > bk-ch01
python ../14_filter_50K.py bk-ch01 bk-ch01.sort
python ../13_bin_geno.py bk-ch01.sort geno-RH-001-ch01 bin.RH-001-ch01 bk.RH-F4-001-ch01
python ../15_snp50_filter.py bin.RH-001-ch01 bk-ch01.mod
for i in $(cat list);do python ../13_bin_geno.py bk-ch01.mod geno-$i bin.$i bk.$i;done 

paste bk.RH-* > tail
cut -f1-4 bin.RH-001-ch01 > head 
paste head tail > ../ch01.txt
