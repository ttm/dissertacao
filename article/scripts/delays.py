#-*- coding: utf-8 -*-
import numpy as n, pylab as p

p.subplot(311)
fa=4410

# Som curto
sdur=0.005 # segundos
f=200. #hz
ii=fa*sdur
s=n.sin(n.linspace(0,2*200*2*n.pi*sdur,ii, endpoint=False))

# resposta ao impulso com um pulso
ddur=0.02
iii=fa*ddur
xi=2*iii/3
hi=n.zeros(iii)
hi[xi]=1
som = n.convolve(s,hi)

p.plot(s+6,'bo', label=r"$\{t_i\}_0^{\Lambda-1}$")
p.plot(hi+3,'ro', label=r"$\{h_i=\delta_{\xi-i}\}_0^{\Lambda_h-1}$")
p.plot(som,'go', label=r"$\{(t*h)_i\}_0^{\Lambda+\Lambda_h-2}$")
p.legend(loc="upper right")
p.xticks((0,ii-1,xi-1,xi+ii-1,ii+iii-2, iii-1),(r"0", r"$\Lambda-1$",r"$\xi$", r"$\xi + \Lambda-1$", r"$\Lambda+\Lambda_h-2$", r"$\Lambda_h$"),fontsize='16')
p.yticks((),())
p.ylim(-1.3,7.3)
p.xlim(-5,ii+iii-2+5)
p.plot([ii-1,ii-1],[-2,9],"y", linewidth=5,alpha=.4)
p.plot([len(hi)-1,len(hi)-1],[-2,9],"y", linewidth=5,alpha=.4)
p.plot([xi -1,xi -1],[-2,9],"y", linewidth=5,alpha=.4)
p.plot([xi +ii-1,xi +ii-1],[-2,9],"y-.", linewidth=5,alpha=.4)

p.ylabel(r"offset", fontsize=16, fontweight='bold')



p.subplot(312)


ddur=0.2
iii=fa*ddur
hi=n.zeros(iii)
pulsos=iii*2/100 # percentagem de incidencias no delay
xis=n.random.randint(0,iii-iii*3/100,pulsos)
xis=n.array([330, 173, 629, 387,  40, 617, 373, 522, 416, 326, 290, 264,  16, 831, 442, 123, 677])
hi[xis]=n.ones(pulsos)
som = n.convolve(hi,s)

p.plot(hi+3,'ro', label=r"$\{h_i=\sum_{j=0}^{\Lambda_j-1}\delta_{\xi_j-i}\}_0^{\Lambda_h-1}$", ms=8)
p.plot(som,'go', label=r"$\{(t*h)_i\}_0^{\Lambda+\Lambda_h-2}$", ms=3)
p.legend(loc="upper right")


p.ylim(-2.7,5.3)
p.xlim(-50,ii+iii-2+50)

p.xticks([0]+list(xis)+[ii+iii-2],[0]+[r"$\delta$"  for i in xis]+[r"$\Lambda+\Lambda_h-2$"],fontsize='16')
p.yticks((),())

p.ylabel(u"rithmic incidences", fontsize=16, fontweight='bold')


p.subplot(313)


ddur=0.2
iii=fa*ddur
hi=n.zeros(iii)
pulsos=iii*30/100 # percentagem de incidencias no delay
xis=n.random.randint(0,iii-iii*3/100,pulsos)
hi[xis]=n.ones(pulsos)
som = n.convolve(hi,s)

p.plot(hi+8,'ro', label=r"$\{h_i=\sum_{j=0}^{\Lambda_j-1}\delta_{\xi_j-i}\}_0^{\Lambda_h-1}$", ms=6)
p.plot(som,'go', label=r"$\{(t*h)_i\}_0^{\Lambda+\Lambda_h-2}$", markersize=2)
p.legend(loc="upper right")


p.ylim(-5.7,11.3)
p.xlim(-50,ii+iii-2+50)

p.xticks([0]+list(xis)+[ii+iii-2],[0]+[r"$\delta$"  for i in xis]+[r"$\Lambda+\Lambda_h-2$"],fontsize='16')
p.yticks((),())

p.ylabel(u"granular synthesis", fontsize=16, fontweight='bold')
p.xlabel(r"$i\quad \rightarrow$",fontsize=26)

p.show()






