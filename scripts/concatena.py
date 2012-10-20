#-*- coding: utf8 -*-
import numpy as n, pylab as p

c=2

# dois períodos de uma dente de serra:
d=n.linspace(-1,1,50)
d=n.hstack((d,d))
d=n.hstack((d,d))
d=d[:len(d)/c]

# quatro periodos de uma onda quadrada
q=n.hstack((  n.ones(13)*-1,n.ones(12)  ))
q=n.hstack((q,q))
q=n.hstack((q,q))
q=n.hstack((q,q))
q=q[:len(q)/c]

# senoide ou ruido
s=n.linspace(0,10*2*n.pi,200,endpoint=False)
s=n.sin(s)[:len(s)/c]
e=5.0
ee=4
p.xticks((),())
p.yticks((),())
p.plot(n.hstack((d,q,s)),'o')
p.plot(n.hstack((d,q,s)))
p.ylim(-1.5,1.5)
p.xlim(-5,305)
p.show()





