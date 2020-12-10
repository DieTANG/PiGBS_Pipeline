#!/public/agis/huangsanwen_group/tangdie/software/Python-3.6.0/python
# To evaluate the distribution of snp depth in the genome.
from __future__ import division
from itertools import islice
import sys

f1 = open(sys.argv[1])       # snp file
fout = open(sys.argv[2],'w')

diSNP,n,heter = {},0,0

for i in islice(f1, 1, None):
	i = i.strip().split()
	if i[0] not in diSNP:
		diSNP[i[0]] = [[int(i[1]),i[9]]]
	else:
		diSNP[i[0]].append([int(i[1]),i[9]])

for i in sorted(diSNP):
	for a in range(0,int(diSNP[i][-1][0])+100000,100000):
		start = a
		end = a+1000000   ### 1M step,100k SLIDING WINDOW
		for k in diSNP[i]:
			if k[0] > end:
				break
			elif k[0] >=start:
				if float(k[1]) > 0 and float(k[1]) < 1:
					heter += 1
				n += 1
		if n == 0:
			continue
		fout.write('%s\t%s\t%s\t%0.2f\n' % (i,start,end,float(heter/n)))
		n,heter = 0,0

f1.close()
fout.close()
