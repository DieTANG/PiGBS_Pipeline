#!/usr/bin/python
# To call heterozygous SNPs in parental clone.

import sys,re

fin1 = open(sys.argv[1])       # vcf file of parent
fout = open(sys.argv[2],'w')   # output of heter SNPs
fout.write('#chromosome\tPos\tRef\tALT\tQ\tMQ\tDref\tDalt\tdepth\tindex\n')

for line in fin1:
	if '#' not in line and 'INDEL' not in line and 'DP4' in line:
		a = line.split()
		Q = float(a[5])
		b = re.split(';|=|,',a[7])
		c = b.index('DP4')
		depth = int(b[c+1])+int(b[c+2])+int(b[c+3])+int(b[c+4])
		MQ = int(b[b.index('MQ')+1])
		index = float(int(b[c+3])+int(b[c+4]))/depth
		if Q >= 40 and MQ >= 30 and depth >= 5 and depth <= 50 and index >= 0.3 and index <= 0.7:
#			print a[0], a[1], depth, index
			fout.write('%s\t%s\t%s\t%s\t%d\t%d\t%d\t%d\t%d\t%0.2f\n'%(a[0],a[1],a[3],a[4],Q,MQ,int(b[c+1])+int(b[c+2]),int(b[c+3])+int(b[c+4]),depth,index))

fin1.close()
fout.close()
