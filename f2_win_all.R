#!/usr/bin/Rscript
dir <- "./win"
setwd(dir)
fl_1 <- dir()
filelist <- as.vector(fl_1)
pdf('339_1Mb10kb.pdf',width=24,height=6)
par(mar=c(3,2.0,3.0,0.5),mgp=c(0.9,0.52,0))

for (i in filelist) {
plot(1:10,type="n",xlim=c(0,725), ylim=c(0,1),main=i,las=1,axes=FALSE, xlab='',ylab='')
axis(side=2,at=c(0,0.2,0.4,0.6,0.8,1.0),labels=c("0","0.2","0.4","0.6","0.8","1.0"),pos=0,las=1,lwd=2.5)
axis(side=1,at=c(0,44.3,112.91,168.35,235.57,297.68,353.48,408.62,468.42,527.63,588.27,640.87,694.16,725),labels=c("","chr01","chr02","chr03","chr04","chr05","chr06","chr07","chr08","chr09","chr10","chr11","chr12",""),pos=-0.01,lwd=2.5,tck=0,las=1)

line <- read.table(i,header=F)

#SL2.50ch01
chr01 <- line[line[,1]=='ST4.03ch01',]
x <- chr01[,3]/1000000
y_b <- chr01[,4]
points(x,y_b,col='#76EEC6',pch=16,cex=0.6)

#chr02
chr02 <- line[line[,1]=='ST4.03ch02',]
x <- chr02[,3]/1000000
y_b <- chr02[,4]
points(x+88.60,y_b,col='#EE7621',pch=16,cex=0.6)

#chr03
chr03 <- line[line[,1]=='ST4.03ch03',]
x <- chr03[,3]/1000000
y_b <- chr03[,4]
points(x+137.22,y_b, col='#76EEC6',pch=16,cex=0.6)

#chr04
chr04 <- line[line[,1]=='ST4.03ch04',]
x <- chr04[,3]/1000000
y_b <- chr04[,4]
points(x+199.49,y_b,col='#EE7621',pch=16,cex=0.6)

#chr05
chr05 <- line[line[,1]=='ST4.03ch05',]
x <- chr05[,3]/1000000
y_b <- chr05[,4]
points(x+271.66,y_b,col='#76EEC6',pch=16,cex=0.6)

#chr06
chr06 <- line[line[,1]=='ST4.03ch06',]
x <- chr06[,3]/1000000
y_b <- chr06[,4]
points(x+323.71,y_b,col='#EE7621',pch=16,cex=0.6)

#chr07
chr07 <- line[line[,1]=='ST4.03ch07',]
x <- chr07[,3]/1000000
y_b <- chr07[,4]
points(x+383.25,y_b,col='#76EEC6',pch=16,cex=0.6)

#chr08
chr08 <- line[line[,1]=='ST4.03ch08',]
x <- chr08[,3]/1000000
y_b <- chr08[,4]
points(x+440,y_b,col='#EE7621',pch=16,cex=0.6)

#chr09
chr09 <- line[line[,1]=='ST4.03ch09',]
x <- chr09[,3]/1000000
y_b <- chr09[,4]
points(x+496.86,y_b,col='#76EEC6',pch=16,cex=0.6)

#chr10
chr10 <- line[line[,1]=='ST4.03ch10',]
x <- chr10[,3]/1000000
y_b <- chr10[,4]
points(x+558.4,y_b,col='#EE7621',pch=16,cex=0.6)

#chr11
chr11 <- line[line[,1]=='ST4.03ch11',]
x <- chr11[,3]/1000000
y_b <- chr11[,4]
points(x+618.15,y_b,col='#76EEC6',pch=16,cex=0.6)

#chr12
chr12 <- line[line[,1]=='ST4.03ch12',]
x <- chr12[,3]/1000000
y_b <- chr12[,4]
points(x+663.58,y_b,col='#EE7621',pch=16,cex=0.6)

#segments(0,0.5,802.14,0.5,col='red',lty=2)
#segments(0,0,802.14,0,col='red',lty=2)
segments(88.60,-0.05,88.60,1,lty=2)
segments(137.22,-0.05,137.22,1,lty=2)
segments(199.49,-0.05,199.49,1,lty=2)
segments(271.66,-0.05,271.66,1,lty=2)
segments(323.71,-0.05,323.71,1,lty=2)
segments(383.25,-0.05,383.25,1,lty=2)
segments(440,-0.05,440,1,lty=2)
segments(496.86,-0.05,496.86,1,lty=2)
segments(558.4,-0.05,558.4,1,lty=2)
segments(618.15,-0.05,618.15,1,lty=2)
segments(663.58,-0.05,663.58,1,lty=2)
#legend("topright",legend=c("e","l","Delta"),pch=19,col=c("red",'green','black'))
}

dev.off()
