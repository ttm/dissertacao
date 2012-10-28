# para testar progressoes logaritmicas e outras
import numpy as n, pylab as p

f0=200.
ff=600.
ii=1000 # tamanho da sequencia
iis=n.arange(ii)

fi=f0*(ff/f0)**(      (iis/float(ii-1))    )

for i in xrange(1,10):
    fi=f0*(ff/f0)**(      (iis/float(ii-1))**i    )
    p.plot(fi)
for i in xrange(1,10):
    fi=f0*(ff/f0)**(      (iis/float(ii-1))**(1./i)    )
    p.plot(fi)

p.text(548,390,r"$\alpha=1           $",fontsize=25)
p.text(850,240,r"$\alpha=10          $",fontsize=25)
p.text(247,327,r"$\alpha=\frac{1}{2} $",fontsize=25)
p.text(68,490, r"$\alpha=\frac{1}{10}$",fontsize=25)


#fi=f0+(ff-f0)*(i/(ii-1))
p.xticks((),())
p.yticks((),())

p.plot(fi)
p.show()

