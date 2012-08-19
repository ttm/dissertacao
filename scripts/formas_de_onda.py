#-*- coding: utf8 -*-
# http://matplotlib.sourceforge.net/examples/api/legend_demo.html
# 
import pylab as p, numpy as n, scikits.audiolab as a

T=100
#T=1024
l=n.linspace(0,2*n.pi,T,endpoint=False)
senoide=n.sin(l)
dente=n.linspace (-1,1,T, endpoint =False) # dente de serra
triangular=n.hstack ((n.linspace(-1,1,T/2,endpoint=False),n.linspace(1,-1,T/2,endpoint=False)))
quadrada=n.hstack ((n.ones(T/2),n.ones(T/2)* -1))

onda=a.wavread("ondaReal.wav")[0] # onda real
onda=((onda-onda.min())/(onda.max()-onda.min()))*2-1

p.subplot(211)
#p.title("Formas de onda")
p.plot(senoide,'o',linewidth=3, label=u"senóide")
p.plot(dente,'o',linewidth=3, label="dente de serra")
p.plot(triangular,'o',linewidth=3, label="triangular")
p.plot(quadrada,'o',linewidth=3, label="quadrada")
p.plot([0],"yo",label="som real (abaixo)")
p.xlim(0,T)
p.ylim(-1.1,1.1)

foo=p.gca()
foo.axes.get_xaxis().set_ticks([])
#l=p.legend((u"senóide","dente de serra","triangular","quadrada"),bbox_to_anchor=(0., 1.02, 1., .102), loc=10,
       #ncol=2, mode="expand", borderaxespad=0.)
#l=p.legend((u"senóide","dente de serra","triangular","quadrada","som real (abaixo)"),bbox_to_anchor=(0., -.1, 1., .1), loc=1,
       #ncol=5, mode="expand", borderaxespad=0.)
l=p.legend(bbox_to_anchor=(0., -.1, 1., .1), loc=1,
       ncol=5, mode="expand", borderaxespad=0.)
for t in l.get_texts():
    t.set_fontsize('small')
frame  = l.get_frame()
frame.set_facecolor('0.80')
for ll in l.get_lines():
        ll.set_linewidth(1.5)  # the legend line width
#p.legend()

p.subplot(212)
p.plot(onda,"yo",linewidth=3)
p.plot(onda,"y",linewidth=3)
p.xlim(0,onda.shape[0])
p.ylim(-1.1,1.1)
foo=p.gca()
foo.axes.get_xaxis().set_ticks([])

p.xlabel(r'tempo $\Delta$, amostras $\Lambda$ ou $i$$\rightarrow$', fontsize=15)
#p.xlabel(r'duração $\delta$, amostras $\lambda$ ou $i$ $\rightarrow$')
p.show()
