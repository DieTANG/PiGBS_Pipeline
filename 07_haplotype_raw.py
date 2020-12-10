#!/usr/bin/python
# To deduce the genotype of all homologous region. For the missing snp, marked as '-'. 

import sys

fin1 = open(sys.argv[1])     # snp file of homo region
fin2 = open(sys.argv[2])     # pos file of each haplotype
fout = open(sys.argv[3],'w')
dict_pos = {}

for i in fin1:
	i = i.split()
	dict_pos[i[2]] = [i[3],i[4]]

for j in fin2:
	j = j.split()
	if j[0] in dict_pos:
		if dict_pos[j[0]][1] == '.':
			fout.write('%s\n' % (dict_pos[j[0]][0]))
		else:
			fout.write('%s\n' % (dict_pos[j[0]][1]))
	else:
		fout.write('%s\n' % ('-'))
	
fin1.close()
fin2.close()
fout.close()
