#!/usr/bin/python

import sys

fin = open(sys.argv[1])
fout = open(sys.argv[2],'w')

for i in fin:
	i = i.split()
	if i[0] == 'ST4.03ch01':
		fout.write('{}\t{}\t{}\t{}\n'.format(i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch02':
		i[2] = int(i[2]) + 90600000
		i[3] = int(i[3]) + 90600000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch03':
		i[2] = int(i[2]) + 141215000
		i[3] = int(i[3]) + 141215000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch04':
		i[2] = int(i[2]) + 205485000
		i[3] = int(i[3]) + 205485000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch05':
		i[2] = int(i[2]) + 279650000
		i[3] = int(i[3]) + 279650000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch06':
		i[2] = int(i[2]) + 333695000
		i[3] = int(i[3]) + 333695000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch07':
		i[2] = int(i[2]) + 395226000
		i[3] = int(i[3]) + 395226000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch08':
		i[2] = int(i[2]) + 453974000
		i[3] = int(i[3]) + 453974000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch09':
		i[2] = int(i[2]) + 512832000
		i[3] = int(i[3]) + 512832000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch10':
		i[2] = int(i[2]) + 576332000
		i[3] = int(i[3]) + 576332000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch11':
		i[2] = int(i[2]) + 638077000
		i[3] = int(i[3]) + 638077000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))
	elif i[0] == 'ST4.03ch12':
		i[2] = int(i[2]) + 685503000
		i[3] = int(i[3]) + 685503000
		fout.write('%s\t%s\t%s\t%s\n' % (i[0],i[1],i[2],i[3]))

fin.close()
fout.close()
