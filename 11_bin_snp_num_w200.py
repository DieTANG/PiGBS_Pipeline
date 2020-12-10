#!/usr/bin/python
# To deduce the genotype of windows. window size = 200 snp, step = 20 snp.

import sys

fin = open(sys.argv[1])
fout = open(sys.argv[2],'w')

list_pos = []
list_geno = []

for l in fin:
	l = l.split()
	list_pos.append(l[1])
	list_geno.append(l[2])
	chr = l[0]

a = range(len(list_geno))
b = a[::20]
bl = len(b)
av,bv,wv=0,0,0

for i in range(bl):
	m = i*20
	n = i*20+200
	if n >= len(list_geno):
		break
	win = list_geno[m:n]
	for j in range(len(win)):
		if win[j] == 'a':
			av += 1
		elif win[j] == 'b':
			bv -= 1
		elif win[j] == 'h':
			continue
	wv = av+bv
	if wv <= -180:
		geno = 'b'
	elif wv >=180:
		geno = 'a'
	elif wv > -180 and wv < 180:
		geno = 'h'
	fout.write('%s\t%s\t%s\t%d\t%s\t%d\n' % (chr,list_pos[m],list_pos[n],wv,geno,1))
	av,bv,wv = 0,0,0

fin.close()
fout.close()
