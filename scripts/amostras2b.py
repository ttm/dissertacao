#-*- coding: utf8 -*-
# http://matplotlib.sourceforge.net/examples/api/legend_demo.html
# 
import pylab as p, numpy as n, scikits.audiolab as a
f=n.fft.fft
#a=[-1,1]
a=n.random.rand(2)*2-1 # 2 amostras quaisquer E [-1,1]
ff=f(a)
#-1 * cos(n.pi*l)
p.plot([0,1],a,"bo")

# Primeiro componente, 0Hz
a0=n.real(ff[0]) 
b0=n.imag(ff[0]) # sempre zero

# Segundo componente, t_a/N Hz
ab1=n.abs(ff[1]) # (a**2+b**2)**0.5 = a1 neste caso
a1=n.real(ff[1]) # eh o modulo ab1 tambem neste caso
b1=n.imag(ff[1]) # zero para o caso de somente 2 amostras pois a fase eh nula e isen(0)=0
#fas=n.arctan(b1/a1) # fase fas=n.angle(f[1])
fas=0 # nao ha adicao de fase para este caso de 2 amostras
# mas o sinal do a1 => sinal da senóide, inversão 2pi
if a1<0: fas+=n.pi # segundo e terceiro quadrantes somam pi
print("abs: %s, a1: %s, b1: %s, fas: %s" % (ab1,a1,b1,fas))


ii=n.linspace(-0.5*n.pi,1.5*n.pi,200)
iii=n.linspace(-0.5,1.5,200)
s=(ab1/2)*n.cos(ii+fas)+a0/2
p.plot(iii,s,"m--")

#pylab.xticks((-1, 0,  1), ('-1', '0',  '1'), color = 'k', size = 20))

p.xlim(-1.2,2)
#p.xlim(0,T2*.56)
p.ylim(-1.1,1.1)

p.ylabel(r"amplitude $\rightarrow$")
p.xlabel(r"tempo $\rightarrow$")
p.show()




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

