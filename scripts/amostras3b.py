#-*- coding: utf8 -*-
# http://matplotlib.sourceforge.net/examples/api/legend_demo.html
# 
import pylab as p, numpy as n, scikits.audiolab as a
f=n.fft.fft

n3=n.random.rand(3)*2-1
p.plot(n3,"bo")

ff=f(n3)
a0=n.real(ff[0]) 
b0=n.imag(ff[0]) # sempre zero

ab1=n.abs(ff[1])
a1=n.real(ff[1])
b1=n.imag(ff[1])
fas=n.arctan(b1/a1) # fase
if a1<0: fas+=n.pi # segundo e terceiro quadrantes somam pi
print("abs: %s, a1: %s, b1: %s, fas: %s" % (ab1,a1,b1,fas))

fr1=(2*n.pi/3)/2 #ciclo em 3 * \delta_a, metade disso
fr2=1/2. # metade de \delta_a
ii=n.linspace(0-fr1,2*n.pi-fr1,200) # [0,2*pi] ciclo completo
iii=n.linspace(0-fr2,3-fr2,200) # [0,3] == 3 \delta_a, período

s=(2/3.)*ab1*n.cos(ii+fas)+a0/3
p.plot(iii,s,"m--")

p.xlim(-1.2,3.2)
p.ylim(-1.1,1.1)

p.ylabel(r"amplitude $\rightarrow$")
p.xlabel(r"tempo $\rightarrow$")
p.show()
