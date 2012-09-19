# para testar progressoes logaritmicas e outras
import numpy as n, pylab as p

f0=200.
ff=600.
ii=1000 # tamanho da sequencia
iis=n.arange(ii)

fi=f0*(ff/f0)**(      (iis/float(ii-1))    )

for i in xrange(10):
    fi=f0*(ff/f0)**(      (iis/float(ii-1))**i    )
    p.plot(fi)

fi=f0+(ff-f0)*(i/(ii-1))


p.plot(fi)
p.show()

