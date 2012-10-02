#-*- coding: utf8 -*-
import numpy as n, pylab as p, scikits.audiolab as a

fa=44100
Dv=2048 # tamanho da tabela do vibrato
fv=6.
nu=12. # desvio maximo em semitons do vibrato
f=2440. # freq do som em si
D=1024 # tamanho da tabela do som
dur=2

x=n.linspace(0,2*n.pi,Dv,endpoint=False)
tabv=n.sin(x) # tabela senoidal para o vibrato

ii=n.arange(fa * dur) # 2 segundos

gv=n.array(ii*fv*float(Dv)/fa, n.int) # indices
tv=tabv[gv%Dv]*nu # amostras do vibrato em desvios de semitons

fi=f*(  2.**(  tv/12.  )   ) # amostras do vibrato em Hz

dD=fi*(Dv/float(fa))
gi=n.cumsum(dD,0,n.int)
#gi=n.array(gi,n.int)

#for i in xrange(1,len(tv)):
#    gi[i]=gi[i-1]+fi[i-1]*(Dv/float(fa))
#gi=n.array(gi,n.int)
#gi=n.array( fi * (Dv/float(fa)  ) +  ii * f  * (Dv/float(fa)  ) , n.int ) % Dv

#gi=  ii * (Dv/float(fa)) * f  
#gi+=(fi-f)*(Dv/float(fa))
#gi=n.array(gi,n.int)

ti=tabv[gi%Dv]
a.wavwrite(ti,"vibrato.wav",fa)

ff=n.ones(ii.shape[0])*f
gi=n.array(  ii * (Dv/float(fa)) * ff  , n.int ) % Dv
t=tabv[ gi ]
a.wavwrite(t,"original.wav",fa)





#tab=n.linspace(-1,1,D) # dente de serra

