#!/usr/bin/python
# The genotype of each based was deduced by comparing with haplotype B of each chromosome.

import sys

fin1 = open(sys.argv[1])       # The haplotype B file.
fin2 = open(sys.argv[2])       # The snp file of each individuals.
fout = open(sys.argv[3], 'w')

dict = {}

for i in fin1:
	if 'pos' not in i:
		i = i.split()
		dict[i[1]] = i[2]

for x in fin2:
	x = x.split()
	if x[1] in dict:
		if int(x[6]) == 0:
			if x[3] != '.':
				if dict[x[1]] == x[2]:
					fout.write('%s\t%s\t%s\n' % (x[0],x[1],'a'))
				else:
					fout.write('%s\t%s\t%s\n' % (x[0],x[1],'b'))
		elif int(x[7]) == 0:
			if dict[x[1]] == x[2]:
				fout.write('%s\t%s\t%s\n' % (x[0],x[1],'b'))
			else:
				fout.write('%s\t%s\t%s\n' % (x[0],x[1],'a'))
		elif int(x[6]) !=0 and int(x[7]) != 0:
			fout.write('%s\t%s\t%s\n' % (x[0],x[1],'h'))
fin1.close()
fin2.close()
fout.close()

