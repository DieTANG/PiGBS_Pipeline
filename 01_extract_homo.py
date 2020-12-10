#!/usr/bin/python
# To evaluate if a region is homo or heter. The window size is 300 SNPs, and step is 30 SNPs.
import sys

fin = open(sys.argv[1])          # raw snp file of each chromosome
fout = open(sys.argv[2],'w')     # homo or heter of each win
list_pos,list_index,homo,heter,num = [],[],0,0,0

for i in fin:
        i = i.split()
	list_pos.append(i[1])
	list_index.append(i[9])
	chr = i[0]

win = range(0,len(list_pos),20)

for j in range(len(win)):
	start = j*30
	end = j*30 + 300
	if end > len(list_pos)-1:
		break
	for k in range(start,end+1):
		if list_index[k] == '0.00' or list_index[k] == '1.00':
			homo += 1
			num += 1
		else:
			heter -= 1
			num += 1
	wv = float(homo + heter)*1.00/num
	if num == 0:
		continue
	if wv >= 0.70:
		fout.write('%s\t%s\t%s\t%s\n' % (chr,list_pos[start],list_pos[end],'homo'))
	else:
		fout.write('%s\t%s\t%s\t%s\n' % (chr,list_pos[start],list_pos[end],'heter'))
	homo,heter,num = 0,0,0

fin.close()
fout.close()
