#!/usr/bin/python
# This script is used to filter the noise snps and generate the final version of two haplotype for each chromosome.

import sys

fin1 = open(sys.argv[1])  # fiter_pos.file
fin2 = open(sys.argv[2])  # chr-A_geno_raw
fin3 = open(sys.argv[3])  # chr-B_geno_raw
fout = open(sys.argv[4],'w')

dict_noise,dict_pos = {},{}

for i in fin1:
	i = i.split()
	dict_noise[i[0]] = 1

for j in fin2:
	j = j.split()
	if j[1] not in dict_noise:
		dict_pos[j[1]] = j[2]

for k in fin3:
	k = k.split()
	if k[1] not in dict_noise:
		if k[1] in dict_pos:
			if k[2] != dict_pos[k[1]]:
				fout.write('%s\t%s\t%s\t%s\n' % (k[0],k[1],dict_pos[k[1]],k[2]))
		else:
			fout.write('%s\t%s\t%s\t%s\n' % (k[0],k[1],'-',k[2]))

fin1.close()
fin2.close()
fin3.close()
fout.close()
