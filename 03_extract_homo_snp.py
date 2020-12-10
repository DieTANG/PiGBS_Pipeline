#!/usr/bin/python
# Extract the homozygous snps.
import sys

fin1 = open(sys.argv[1])      # rawsnp file of each individual
fin2 = open(sys.argv[2])      # break point of homo region
fout = open(sys.argv[3],'w')  # snp in the homo region
dict,list_pos,list_geno,list_index,list_snp,homo,heter,num,bk_s,bk_e = {},[],[],[],[],0,0,0,[],[]

for line in fin1:
	i = line.split()
	list_pos.append(i[1])
	list_index.append(i[9])
	dict[i[1]] = line
	if i[3] == '.':
		list_geno.append(i[2])
	else:
		list_geno.append(i[3])

for j in fin2:
	j = j.split()
	bk_s.append(j[0])
	bk_e.append(j[1])

for k in range(1,len(bk_s)):
	start = int(bk_e[k-1])
	end = int(bk_s[k])
	for l in range(len(list_pos)):
		if int(list_pos[l]) > start and int(list_pos[l]) <= end:
			if list_index[l] == '0.00' or list_index[l] == '1.00':
				num +=1
				homo +=1
			elif list_index[l] != '0.00' and list_index[l] != '1.00':
				num +=1
				heter -=1
#		if num > 1000:
#			break
	if float(homo+heter)*1.00/(num+1) >= 0.70:
#		print float(homo+heter)*1.00/(num+1), 'good'
		for m in range(len(list_pos)):
			if int(list_pos[m]) > start and int(list_pos[m]) <= end:
				fout.write('%s%d\t%s' % ('homo',k,dict[list_pos[m]]))
		homo,heter,num = 0,0,0
	else:
#		print float(homo+heter)*1.00/(num+1), 'bad'
		homo,heter,num = 0,0,0

fin1.close()
fin2.close()
fout.close()

