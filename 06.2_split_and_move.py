#!/usr/bin/python
########## split homo regions and move to A B group ####################
import sys,os

f1=open('split_id','r')
f2=open(sys.argv[1],'r')
f3=open(sys.argv[2],'r') # ref filter_file
fout=open('awk.sh','a')

for line in f1:
    i = line.strip().split("\t")
    command1 = 'awk \'/'+i[0]+'\\t/\' '+ os.path.basename(f2.name) + '>' +  os.path.basename(f2.name)+'_'+i[0]+'\n'
    os.system(command1)
    fout.write(command1)
    command2 = 'python 5_cmp_and_move.py ' + os.path.basename(f3.name)+' '+os.path.basename(f2.name)+'_'+i[0]+'\n'
    os.system(command2)
    fout.write(command2)

f1.close()
f2.close()
f3.close()
fout.close()
