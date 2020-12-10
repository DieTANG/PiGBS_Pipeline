#!/usr/bin/python
# Compare the homologous region with the reference individual for each chromosome. The aim is to divide all regions into two groups.
import sys

fin1 = open(sys.argv[1])   # ref homo regions
fin2 = open(sys.argv[2])   # homo region
#fout = open(sys.argv[3],'w')
dict_pos = {}
n = 0
sum = 0
def GetFileName(filename):
    import os
    (filepath,tempfilename) = os.path.split(filename);
  #  (shortname,extension) = os.path.splitext(tempfilename);
    return filename

for i in fin1:
	i = i.split()
	dict_pos[i[2]]=i[4]

for j in fin2:
	j = j.split()
	if j[2] in dict_pos:
		if j[4] == dict_pos[j[2]]:
			sum += 1
			n += 1
		else:
			n +=1
if n == 0:
    print(GetFileName(sys.argv[2]),0,0,0)
#    fout.write('%s,0,0,0\n'%(GetFileName(sys.argv[2])))
else:
	print(GetFileName(sys.argv[2]),sum, n, float(sum)/n)
    #fout.write('%s,%s,%s,%s\n'%(GetFileName(sys.argv[2]),sum, n, float(sum)/n))

fin1.close()
fin2.close()
