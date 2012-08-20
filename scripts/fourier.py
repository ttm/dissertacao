#-*- coding: utf8 -*-
# http://matplotlib.sourceforge.net/examples/api/legend_demo.html
# 
import pylab as p, numpy as n, scikits.audiolab as a
f=n.fft.fft
fi=n.fft.ifft
a=[-1,1]
#-1 * cos(n.pi*l)
#p.plot([0,1],a,"bo") ##########3
ii=n.linspace(-0.5*n.pi,1.5*n.pi,200)
iii=n.linspace(-0.5,1.5,200)
s=-n.cos(ii)
#p.plot(iii,s,"m--") ###########3


p.ylabel(r"amplitude $\rightarrow$")
p.xlabel(r"tempo $\rightarrow$")
#p.show()




n3=n.random.rand(3)*2-1

ff=f(n3)
a0=n.real(ff[0])
b0=n.imag(ff[0])

ab1=n.abs(ff[1])
a1=n.real(ff[1])
b1=n.imag(ff[1])
#fas=b1/a1
fas=n.arctan(b1/a1) # fase
fas=n.arctan(b1/a1)*3
print("abs: %s, a1: %s, b1: %s, fas: %s" % (ab1,a1,b1,fas))

#vfas=(n.sin(fas)-sin(fas))

ii=n.linspace(-0.5*n.pi,1.5*n.pi,200)
iii=n.linspace(-0.5,2.5,200)
#s=-ab1*n.cos(ii-fas)
#p.plot(iii,s,"m--")
#p.plot(n3,"bo")

s=(2/3.)*ab1*n.cos(ii)+a0/3; p.plot(iii,s,"m--"); p.plot(n3,"bo");p.show()


p.xlim(-1.2,3.2)
#p.xlim(0,T2*.56)
p.ylim(-1.1,1.1)
#p.show()



d=[-.6,-.2,.2,.6]
t=[-1,0,1,0]
q=[-1,-1,1,1]

da1=n.pi

da2=n.pi/2

das=n.linspace(-n.pi/2,-5*n.pi/2,4,endpoint=False)
s1=n.sin(das)
s2=n.array(a*2)

#p.plot(s1)
#p.plot(s2)
#p.plot(s1+s2)
#p.plot(d)
#p.show()

