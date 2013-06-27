# coding: utf-8
# para testar progressoes logaritmicas e outras
import numpy as n, pylab as p

f0=1
ff=2
ii=1000 # tamanho da sequencia
iis=n.arange(ii)

fi=f0*(ff/f0)**(      (iis/float(ii-1))    )

for i in xrange(1,10):
    fi=f0*(ff/f0)**(      (iis/float(ii-1))**i    )
    p.plot(fi)
for i in xrange(2,10):
    fi=f0*(ff/f0)**(      (iis/float(ii-1))**(1./i)    )
    p.plot(fi)

p.text(548,1.53,r"$\alpha=1           $",fontsize=25)
p.text(858,1.14,r"$\alpha=10          $",fontsize=25)
p.text(243,1.38,r"$\alpha=\frac{1}{2} $",fontsize=25)
p.text(68,1.78, r"$\alpha=\frac{1}{10}$",fontsize=25)


p.xticks((),())
p.yticks((1,2), fontsize=26)

p.ylim(0.9,2.1)
p.xlim(-10,1010)

p.plot(fi)
p.show()

