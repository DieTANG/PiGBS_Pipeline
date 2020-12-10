#!/usr/bin/python
# To generate the bin genotype file which can be directly used for genetic mapping.

import sys

fin1 = open(sys.argv[1])     # file of bin breaks
fin2 = open(sys.argv[2])     # snp genotype of each individuals
fout1 = open(sys.argv[3],'w')
fout2 = open(sys.argv[4],'w')
list_breaks,dict_pos,va,vb,vh,num = [],{},0,0,0,0

for i in fin1:
	i = i.split()
	list_breaks.append(i[0])

for j in fin2:
	j = j.split()
	dict_pos[j[1]] = j[2]
	chr = j[0]

for k in range(len(list_breaks)-1):
	start = int(list_breaks[k])
	end = int(list_breaks[k+1])
	for l in dict_pos:
		if int(l) >= start and int(l) < end:
			if dict_pos[l] == 'a':
				va += 1
				num +=1
			elif dict_pos[l] == 'b':
				vb += 1
				num += 1
			elif dict_pos[l] == 'h':
				vh += 1
				num += 1
	if num == 0:
		fout1.write('%s\t%s%d\t%d\t%d\t%s\t%s\t%s\t%s\n' % (chr,'bin',k+1,start+1,end,va,vb,vh,'-'))
		fout2.write('%s\n' % ('-'))
	else:
		ratio =float(va-vb)*1.00/num
		if ratio >= 0.7:
			fout1.write('%s\t%s%d\t%d\t%d\t%s\t%s\t%s\t%s\n' % (chr,'bin',k+1,start+1,end,va,vb,vh,'a'))
			fout2.write('%s\n' % ('a'))
		elif ratio <= -0.7:
			fout1.write('%s\t%s%d\t%d\t%d\t%s\t%s\t%s\t%s\n' % (chr,'bin',k+1,start+1,end,va,vb,vh,'b'))
			fout2.write('%s\n' % ('b'))
		elif ratio > -0.7 and ratio < 0.7:
			fout1.write('%s\t%s%d\t%d\t%d\t%s\t%s\t%s\t%s\n' % (chr,'bin',k+1,start+1,end,va,vb,vh,'h'))
			fout2.write('%s\n' % ('h'))
	va,vb,vh,num = 0,0,0,0

fin1.close()
fin2.close()
fout1.close()
fout2.close()
