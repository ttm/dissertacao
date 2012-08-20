#-*- coding: utf8 -*-
# http://matplotlib.sourceforge.net/examples/api/legend_demo.html
# 
import pylab as p, numpy as n, scikits.audiolab as a

T=30
#T=1024
l=n.linspace(0,2*n.pi,T,endpoint=False)
senoide=n.sin(l)


dente=n.linspace (-1,1,T) # dente de serra
triangular=n.hstack ((n.linspace(-1,1,T/2,endpoint=False),n.linspace(1,-1,T/2,endpoint=False)))
quadrada=n.hstack ((n.ones(T/2),n.ones(T/2)* -1))


T2=T*10000
indices=n.arange(T2)

s_=senoide[indices%T]
s_s=n.fft.fft(s_)
s_a=n.abs(s_s)

d_=dente[indices%T]
d_s=n.fft.fft(d_)
d_a=n.abs(d_s)

t_=triangular[indices%T]
t_s=n.fft.fft(t_)
t_a=n.abs(t_s)

q_=quadrada[indices%T]
q_s=n.fft.fft(q_)
q_a=n.abs(q_s)


i=indices
foo=(s_a>50).nonzero()
p.plot(i[foo],s_a[foo],"o", label=u"senóide")
foo=(d_a>50).nonzero()
p.plot(i[foo],d_a[foo],"*", label=r"dente de serra")
ii=list(i[foo])
foo=(t_a>50).nonzero()
p.plot(i[foo],t_a[foo],"^", label=r"triangular")
#p.plot(i[foo],t_a[foo],"^", label=r"triangular")
foo=(q_a>50).nonzero()
p.plot(i[foo],q_a[foo],"s", label="quadrada")
p.legend(loc="upper right")

p.yticks((0,20000),(0,"20k"))
p.xticks((0,T2/2),(0,"150k"))
#ticks=[r"$f%i$" % (i,) for i in xrange(len(ii))]
#p.xticks([0] + ii + [17000],[0] + ticks + ["17k"])

#p.xlim(0,T2*.6)
p.ylim(-300,max(q_a))
p.ylabel(r'valor absoluto $\rightarrow$')
p.xlabel(r'componente do espectro $\rightarrow$')




p.show()
