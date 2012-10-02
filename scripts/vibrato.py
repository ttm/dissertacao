#-*- coding: utf8 -*-
import numpy as n, pylab as p, scikits.audiolab as a

fa=44100
Dv=2048 # tamanho da tabela do vibrato
fv=1.5 # frequência do vibrato
nu=12. # desvio maximo em semitons do vibrato (profundidade)
f=1040. # freq do som em si
D=1024 # tamanho da tabela do som
dur=2

x=n.linspace(0,2*n.pi,Dv,endpoint=False)
tabv=n.sin(x) # tabela senoidal para o vibrato

# Padrao do vibrato
ii=n.arange(fa * dur) # 2 segundos
gv=n.array(ii*fv*float(Dv)/fa, n.int) # indices
tv=tabv[gv%Dv]*nu # desvio instantaneo de semitons para cada amostra
fi=f*(  2.**(  tv/12.  )   ) # frequência em Hz em cada amostra

### Som em si
tab=n.linspace(-1,1,D) # dente de serra

dD=fi*(D/float(fa)) # a movimentação na tabela por amostra
gi=n.cumsum(dD,0,n.int) # a movimentacao na tabela total, jah inteiro
ti=tabv[gi%D]
a.wavwrite(ti,"vibrato.wav",fa)

gi=n.array(  ii * (D/float(fa)) * f  , n.int ) % Dv
t=tabv[ gi ]
a.wavwrite(t,"original.wav",fa)

p.specgram(ti-ti.mean())
p.colorbar()
p.xlim(-2000,46100)
p.xticks((0,10000,20000,30000,44000),(r"0",10000,20000,30000,44100))
p.show()

p.ylabel(u"frequência "+r"$ \in \; [0,\,\frac{f_a=44100}{2}=22050] \quad \rightarrow $", fontsize=16)
p.xlabel(r"$i\quad \rightarrow$",fontsize=26)


