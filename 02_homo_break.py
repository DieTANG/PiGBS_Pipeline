#!/usr/bin/python
# To extract the break point between homo and heter genomic regions.
import sys

fin = open(sys.argv[1])         # homo or heter of each win
fout = open(sys.argv[2],'w')    # the break point between homo and heter of each chromosome
list_pos_s,list_pos_e,list_pat,list_break,dict_bk = [],[],[],[0],{}
fout.write('0\t0\n')
#dict_chr = {'ST4.03ch01':88663953,'ST4.03ch02':48614682,'ST4.03ch03':62290287,'ST4.03ch04':72208622,'ST4.03ch05':52070159,'ST4.03ch06':59532097,'ST4.03ch07':56760844,'ST4.03ch08':56938458,'ST4.03ch09':61540752,'ST4.03ch10':59756224,'ST4.03ch11':45475668,'ST4.03ch12':61165650}
dict_chr = {'chr01':89912338,'chr02':73002285,'chr03':68680985,'chr04':60751181,'chr05':61734833,'chr06':59256477,'chr07':60194623,'chr08':64592454,'chr09':55540250,'chr10':61184543,'chr11':52749447,'chr12':48534186}

for i in fin:
	i = i.split()
	list_pos_s.append(int(i[1]))
	list_pos_e.append(int(i[2]))
	list_pat.append(i[3])
	key = i[0]

for j in range(1,len(list_pat)):
	if list_pat[j] == list_pat[j-1]:
		continue
	else:
		list_break.append(list_pos_s[j-1])
		dict_bk[list_pos_s[j-1]] = [list_pos_s[j-1],list_pos_e[j-1]]

if len(list_break) == 2:
	fout.write('%s\t%s\n' % (list_break[1],dict_bk[list_break[1]][1]))
else:
	for k in range(1,len(list_break)-1):
		if list_break[k]-list_break[k-1]>300000 and list_break[k+1]-list_break[k]>300000:
			fout.write('%s\t%s\n' % (dict_bk[list_break[k]][0],dict_bk[list_break[k]][1]))
	if list_break[len(list_break)-1]-list_break[len(list_break)-2]>300000 and int(dict_chr[key])-list_break[len(list_break)-1]>300000:
		fout.write('%s\t%s\n' % (dict_bk[list_break[len(list_break)-1]][0],dict_bk[list_break[len(list_break)-1]][1]))
fout.write('%s\t%s\n' % (int(dict_chr[key]),int(dict_chr[key])))

fin.close()
fout.close()
