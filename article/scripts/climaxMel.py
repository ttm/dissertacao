#-*- coding: utf8 -*-
import numpy as n, pylab as p


c1=n.hstack(( n.linspace(0,1,1000,endpoint=False),n.linspace(1,0,1000)    )) # simetrico
c2=n.hstack(( n.linspace(0,1,500,endpoint=False), n.linspace(1,0,1500)    ))
c3=n.hstack(( n.linspace(0,1,1500,endpoint=False),n.linspace(1,0,500)    ))
c4=n.linspace(1,0,2000)
c5=n.linspace(0,1,2000)

p.plot(c1,label=u"clímax no meio",lw=5)
p.plot(c2,label=u"clímax na primeira metade",lw=5)
p.plot(c3,label=u"clímax na segunda metade", lw=5)
p.plot(c4,label=u"clímax no começo",         lw=5)
p.plot(c5,label=u"clímax no fim",            lw=5)
p.legend(loc="lower center",prop={'size':22})

p.xlim(-50,2050)
p.ylim(-.18,1.02)

p.xticks((),())
p.yticks((),())

p.xlabel(r"tempo $\rightarrow$", fontsize=19)
p.ylabel(u"parâmetro"+r"$\rightarrow$", fontsize=19)

p.show()

