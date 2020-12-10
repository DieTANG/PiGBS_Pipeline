#!/usr/bin/python
# Compare the homologous region with the reference individual for each chromosome. The aim is to divide all regions into two groups.
import sys,os

fin1 = open(sys.argv[1])   # ref homo regions
fin2 = open(sys.argv[2])   # homo region
dict_pos,n,sum = {},0,0

def GetFileName(filename):
    (filepath,tempfilename) = os.path.split(filename);
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
    print GetFileName(sys.argv[2]),0,0,0
    command0 = 'mv ' + GetFileName(sys.argv[2]) + ' ./ch06-raw' 
    os.system(command0)
else:
	print GetFileName(sys.argv[2]),sum, n, float(sum)/n

if n !=0:
    if float(sum)/n == 1:
        command1 = 'cp ' + GetFileName(sys.argv[2]) + ' ./ch06-B'
        os.system(command1)
    if float(sum)/n >= 0.9 and float(sum)/n != 1:
        command2 = 'mv ' + GetFileName(sys.argv[2]) + ' ./ch06-B'
        os.system(command2)
    if float(sum)/n <= 0.1 and float(sum)/n != 0:
        command3 = 'mv ' + GetFileName(sys.argv[2]) + ' ./ch06-A'
        os.system(command3)

fin1.close()
fin2.close()
