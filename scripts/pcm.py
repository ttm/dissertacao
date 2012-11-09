#-*- coding: utf8 -*-
import numpy as n, pylab as p

# plotando um som em PCM de 4 bits de profundidade

# grade de variacao de amplitude
p.grid(True, axis='y',ls='-.',lw=2)


aa=n.linspace(0,2*2*n.pi,500)[:250]
b=n.sin(aa)+n.sin(4*aa)
b*=.5
b*=2**3-1 # 4 bits

p.plot(aa,b,"g",lw=6)

c=n.round(b)
p.plot(aa[::10],c[::10],'ro',ms=9)

p.yticks(range(-7,8), fontsize=18)
xlabs=[r"$\lambda_a$"]*len(aa[::10])
xlabs=[str(i)+xlabs[i] for i in xrange(len(xlabs))]
xlabs[0]=0
xlabs[1]=r"$\lambda_a$"
p.xticks((aa[::10]),xlabs)

p.xlim(-.3,aa[::10][-1]+0.5)

p.xlabel(r"tempo $\rightarrow$",fontsize=20)
p.ylabel(r"amplitude $\rightarrow$",fontsize=24)

p.show()



