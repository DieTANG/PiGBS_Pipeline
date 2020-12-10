import sys
import re
f = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
a,n = [],[]
for line in f:
    k = line.strip().split()
    pos = int(k[0])
    a.append(pos)

for i in range(0,len(a)-2):
    if int(a[i+1]) -int(a[i])>50000 or int(a[i+2])-int(a[i+1])>50000:
        n.append(a[i+1])
fout.write(str(a[0])+'\n')
for j in n:
    fout.write(str(j)+'\n')

f.close()
fout.close()
