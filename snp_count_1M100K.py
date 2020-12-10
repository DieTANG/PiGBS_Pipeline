#!/public/agis/huangsanwen_group/tangdie/software/Python-3.6.0/python
import sys
fout = open(sys.argv[2],'w')
snp_dict = {}
n,depth = 0,0
with open(sys.argv[1],'r') as SNP_file:
	next(SNP_file)
	for line in SNP_file:
		i = line.strip().split()
		if i[0] not in snp_dict:
			snp_dict[i[0]] = [[int(i[1]),int(i[9])]]
		else:
			snp_dict[i[0]].append([int(i[1]),int(i[9])])
	
for j in sorted(snp_dict):
	for a in range(0,snp_dict[j][-1][0],100000):
		start = a
		end = a + 1000000
		for k in snp_dict[j]:
			if start <= k[0] <= end:
				n += 1
			depth += 1
		if n == 0:
			continue
		fout.write('%s\t%s\t%s\t%s\t%s\t%0.2f\n'%(j,start,end,n,depth,float(depth)/n))
		n,depth = 0,0
fout.close()
