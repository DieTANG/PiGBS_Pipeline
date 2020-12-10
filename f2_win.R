#!/usr/bin/Rscript

dir <- "./win"
setwd(dir)
fl_1 <- dir()
filelist <- as.vector(fl_1)
pdf('C343_ch12.pdf',width=24,height=6)
par(mar=c(3,3.0,3.0,0.5),mgp=c(1.5,0.52,0))
for(i in filelist){
a <- read.table(i)
chr <- a[a[,1]=='ST4.03ch12',]
x <- chr[,3]/1000000
y_b <- chr[,4]
plot(1:10,type ='n',xlim=c(0,89), ylim=c(0,1),las=1,axes=FALSE, main=i,cex.main=2, xlab='Mb',ylab='SNP_Index')
points(x,y_b,col='red',pch=19,cex=0.4)
#segments(0,0,802.14,0,col='red',lty=2)
axis(side=1,at=seq(0,88.6,by=1),labels=seq(0,88.6,by=1),pos=-0.02,lwd=2,tck=0.01)
axis(side=2,at=c(0,0.2,0.4,0.6,0.8,1.0),labels=c('0','0.2','0.4','0.6','0.8','1.0'),pos=0,las=1,lwd=2)
}
dev.off()
