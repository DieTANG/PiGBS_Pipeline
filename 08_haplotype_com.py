#!/usr/bin/python
# Combine the genoytpe of all progeny into a file.
import sys

fin = open(sys.argv[1])
fout = open(sys.argv[2], 'w')

set1 = set()

for i in fin:
	i = i.split()
	for a in range(1,len(i)):
		if i[a] != '-':
			set1.add(i[a])
			geno = i[a]
	if len(set1) == 1:
		fout.write('%s\t%s\t%s\n' % ('ch02', i[0], geno))
		set1 = set()
	else:
		set1 = set()

fin.close()
fout.close()
