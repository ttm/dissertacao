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
p.plot(s+ee+3*e,'o')
p.plot(q+ee+2*e,'o')
p.plot(d+ee+e,'o')
p.plot(s+q+d,'o')

p.ylim(-3.5,21)
p.xlim(-5,105)

p.text(47,11.4-.5,"+",fontsize=48)
p.text(47,11.4+e-.5,"+",fontsize=48)
p.text(46,11.4-e-2,"=",fontsize=78)

p.xticks((),())
p.yticks((),())


p.show()
