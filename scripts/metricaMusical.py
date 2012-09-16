#-*- coding: utf8 -*-
import numpy as n, pylab as p

resolucao=9*8 # 72

p.plot((0,34),(1,1)); p.plot((36,72),(1,1))

p.plot((0,16),(2,2)); p.plot((36,52),(2,2))
p.plot((18,34),(2,2)); p.plot((54,72),(2,2))

#p.plot(xs2,s2)
p.ylim(-1,4)
p.show()

