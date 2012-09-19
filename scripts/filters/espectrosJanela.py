#-*- coding: utf8 -*-
import numpy as n, pylab as p
ifft=n.fft.ifft
ones=n.ones
subplot=p.subplot
plot=p.plot
show=p.show


N=101

e=ones(N)
e[0]=0
sa=[]
for i in xrange(1,(N-1)/2+1):
    e[i]=0
    e[-i]=0
    s=ifft(e)
    sa.append(s)




#i=0
#for s in ss:
    #i+=1
    #subplot("%i1%i" % (len(ss),i))
    #plot(s)
#show()
