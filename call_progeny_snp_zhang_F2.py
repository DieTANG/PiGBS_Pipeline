#!/usr/bin/python

import sys
import re

fin1 = open(sys.argv[1])       # input heterzygous snps of parents
fin2 = open(sys.argv[2])       # vcf file of progeny
fout = open(sys.argv[3],'w')   # output filtered SNPs
dict_pos = {}
fout.write('#chromosome\tPos\tRef\tALT\tQ\tMQ\tDref\tDalt\tdepth\tindex\n')

for i in fin1:
	if '#' not in i:
		i = i.split()
		dict_pos[i[0]+i[1]] = 1

for line in fin2:
	if '#' not in line and 'INDEL' not in line:
		a = line.split()
		if a[0]+a[1] in dict_pos:
			Q = float(a[5])
			b = re.split(';|=|,',a[7])
			c = b.index('DP4')
			depth = int(b[c+1])+int(b[c+2])+int(b[c+3])+int(b[c+4])
			if depth > 0:
				index = float(int(b[c+3])+int(b[c+4]))/depth		
				MQ = int(b[b.index('MQ')+1])
				fout.write('%s\t%s\t%s\t%s\t%d\t%d\t%d\t%d\t%d\t%0.2f\n'%(a[0],a[1],a[3],a[4],Q,MQ,int(b[c+1])+int(b[c+2]),int(b[c+3])+int(b[c+4]),depth,index))

fin1.close()
fin2.close()
fout.close()
