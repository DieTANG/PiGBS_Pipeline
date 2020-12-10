#!/usr/bin/python
# To deduce the crossover site based on the sliding window of snp numbers.

import sys

fin = open(sys.argv[1])                    # sliding window of each chromosome
fout = open(sys.argv[2],'w')			   # break points of bin 
list_pos,list_geno,bin_pos = [],[],[0]
fout.write('0\n')

for i in fin:
	i = i.split()
	list_pos.append(i[1])
	list_geno.append(i[4])

for j in range(len(list_geno)):
	if j > 0:
		if list_geno[j] == list_geno[j-1]:
			continue
		else:
			bin_pos.append(list_pos[j-1])

for k in range(len(bin_pos)):
	if k > 0 and k < len(bin_pos)-1:
		if int(bin_pos[k]) - int(bin_pos[k-1]) > 100000 and int(bin_pos[k+1]) - int(bin_pos[k]) > 100000:
			fout.write('%s\n' % (bin_pos[k]))
	elif k == len(bin_pos)-1:
		if int(bin_pos[k]) - int(bin_pos[k-1]) > 100000:
			fout.write('%s\n' % (bin_pos[k]))

fin.close()
fout.close()




