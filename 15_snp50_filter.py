import sys
fout=open(sys.argv[2],'w')
fout.write('0'+'\n')
with open(sys.argv[1],'r') as f:
    for line in f:
        i = line.split()
        snp = int(i[4])+int(i[5])+int(i[6])
        if snp >=50:
            fout.write(i[3]+'\n')
fout.close()
