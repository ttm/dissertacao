#-*- coding: utf8 -*-
# http://matplotlib.sourceforge.net/examples/api/legend_demo.html
# 
import pylab as p, numpy as n, scikits.audiolab as a

a=[-1,1]
d=[-.6,-.2,.2,.6]
t=[-1,0,1,0]
q=[-1,-1,1,1]

da1=n.pi

da2=n.pi/2

das=n.linspace(-n.pi/2,-5*n.pi/2,4,endpoint=False)
s1=n.sin(das)
s2=n.array(a*2)

p.plot(s1)
p.plot(s2)
p.plot(s1+s2)
p.plot(d)
p.show()

