# To filter the snp with index of '1.00' but the alternative nucleotide is '.'.
import sys
fin1 = open(sys.argv[1])       # raw snp of hmsnp
fout1 = open(sys.argv[2],'w')  # heter snps in hm region
fout2 = open(sys.argv[3],'w')  # filter snp of hmsnp
dict = {}

for i in fin1:
	j = i.split()
	if j[10] != '1.00' and j[10] != '0.00':
		if int(j[5]) >= 30 and int(j[6]) >= 30:
			fout1.write(i)
			fout2.write(i)
	elif j[10] == '0.00' and j[4] == '.':
		if int(j[5]) >= 30 and int(j[6]) >= 30:
			fout2.write(i)
	elif j[10] == '1.00':
		if j[4] == '.':
			continue
		else:
			if int(j[5]) >= 30 and int(j[6]) >= 30:
				fout2.write(i)

fin1.close()
fout1.close()
fout2.close()
