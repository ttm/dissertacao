#-*- coding: utf8 -*-
# http://matplotlib.sourceforge.net/examples/api/legend_demo.html
# 
import pylab as p, numpy as n, scikits.audiolab as a

# uma nota inteira de oboe; 150529 amostras
oboe=a.wavread("22686__acclivity__oboe-a-440.wav")[0]
oboe=oboe[:,0]+oboe[:,1] # estereo para mono

# um periodo da nota (recortado no audacity buscando zeros)
# nao se repete o zero, por isso o [:-1], resulta 98 amostras
poboe=a.wavread("22686__acclivity__oboe-a-440_periodo.wav")[0][:-1]
# fazendo um sinal do mesmo tamanho:
poboe2=n.array(list(poboe)*1510) # 147980 
#poboe2=n.array(list(poboe)*1536) # len(oboe)/len(poboe) nao bate tanto pois pegamos uma frequencia relativamente baixa == periodo grande 
#poboe2=poboe[n.arange(oboe.shape[0])%poboe.shape[0]] # Descobrir pq nao funciona


o_s=n.fft.fft(oboe)
o_a=n.abs(o_s)

p_s=n.fft.fft(poboe2)
p_a=n.abs(p_s)




i=n.arange(poboe2.shape[0])
foo=(p_a>50).nonzero()
p.plot(i[foo],p_a[foo],"o",label=u"período amostrado")
ii=list(i[foo])

i=n.arange(oboe.shape[0])
p.plot(i,o_a,label=u"nota de oboé natural")
p.legend(loc="upper right")

ticks=[]
ticks=[r"$f%i$" % (i,) for i in xrange(len(ii))]

p.yticks((0,11000),(0,'11k'))
p.xticks([0] + ii + [22000],[0] + ticks + ["22k"])

p.xlim(0,22000,)
p.ylim(-300,11000)
p.ylabel(r'valor absoluto $\sqrt{a^2+b^2}$ da componente complexa $\rightarrow$')
p.xlabel(u'componente do espectro em frequência' + r'$\rightarrow$')
p.show()


#s_=senoide[indices%T]
#s_s=n.fft.fft(s_)
#s_a=n.abs(s_s)

#d_=dente[indices%T]
#d_s=n.fft.fft(d_)
#d_a=n.abs(d_s)

#t_=triangular[indices%T]
#t_s=n.fft.fft(t_)
#t_a=n.abs(t_s)

#q_=quadrada[indices%T]
#q_s=n.fft.fft(q_)
#q_a=n.abs(q_s)


#i=indices
#foo=(s_a>50).nonzero()
#p.plot(i[foo],s_a[foo],"o", label=u"senóide")
#foo=(d_a>50).nonzero()
#p.plot(i[foo],d_a[foo],"*", label=r"dente de serra")
#foo=(t_a>50).nonzero()
#p.plot(i[foo],t_a[foo],"^", label=r"triangular")
##p.plot(i[foo],t_a[foo],"^", label=r"triangular")
#foo=(q_a>50).nonzero()
#p.plot(i[foo],q_a[foo],"s", label="quadrada")
#p.xlim(0,T2*.51)
#p.ylim(-300,20000)

#p.yticks((0,20000),(0,"20k"))
#p.xticks((0,15000),(0,"15k"))

#p.legend(loc="upper right")
#p.ylabel(r'valor absoluto $\rightarrow$')
#p.xlabel(r'componente do espectro $\rightarrow$')




#p.show()
