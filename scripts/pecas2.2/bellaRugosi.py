#-*- coding: utf8 -*-
import numpy as n, scikits.audiolab as a
H=n.hstack
V=n.vstack

f_a = 44100. # Hz, frequência de amostragem

############## 2.2.1 Tabela de busca (LUT)
Lambda_tilde=Lt=1024.

# Senoide
foo=n.linspace(0,2*n.pi,Lt,endpoint=False)
S_i=n.sin(foo) # um período da senóide com T amostras

# Quadrada:
Q_i=n.hstack(  ( n.ones(Lt/2)*-1 , n.ones(Lt/2) )  )

# Triangular:
foo=n.linspace(-1,1,Lt/2,endpoint=False)
Tr_i=n.hstack(  ( foo , foo*-1 )   )

# Dente de Serra:
D_i=n.linspace(-1,1,Lt)


def v(f=200,d=2.,tab=S_i,fv=2.,nu=2.,tabv=S_i):
    Lambda=n.floor(f_a*d)
    ii=n.arange(Lambda)
    Lv=float(tabv)

    Gammav_i=n.floor(ii*fv*Lv/f_a) # índices para a LUT
    Gammav_i=n.array(Gammav_i,n.int)
    Tv_i=tabv[Gammav_i%int(Lv)] # padrão de variação do vibrato para cada amostra

    F_i=f*(   2.**(  Tv_i*nu/12.  )   ) # frequência em Hz em cada amostra

    D_gamma_i=F_i*(Lt/float(f_a)) # a movimentação na tabela por amostra
    Gamma_i=n.cumsum(D_gamma_i) # a movimentação na tabela total
    Gamma_i=n.floor( Gamma_i) # já os índices
    Gamma_i=n.array( Gamma_i, dtype=n.int) # já os índices
    return tab[Gamma_i%int(Lt)] # busca dos índices na tabela



dd=v(tabv=Tr_i ,d=2,fv=35.,nu=7.0)
dd2=v(tabv=D_i ,d=2,fv=35.,nu=7.0)

dd3=v(tabv=Tr_i,d=2,fv=35.,nu=7.0)
dd4=v(tabv=S_i ,d=2,fv=35.,nu=7.0)

dd5=v(tabv=Q_i ,d=2,fv=35.,nu=7.0)
dd6=v(tabv=S_i ,d=2,fv=35.,nu=7.0)

dd7=v(tabv=Q_i ,d=2,fv=35.,nu=7.0)
dd8=v(tabv=D_i ,d=2,fv=35.,nu=7.0)

zz=V((H((dd,dd3,dd5,dd7)), H((dd2,dd4,dd6,dd8))))
aa1=n.array(list(v(tabv=Q_i,fv=.5,f=200,nu=9))*4)
aa2=n.array(v(tabv=Tr_i,fv=.25/2.,f=200,nu=9,d=8.))
aa3=n.array(v(fv=.25/2.,f=200,nu=9,d=8.))

aa=n.vstack(( (zz+aa1).T*.5, (zz+aa2).T*.5,(zz+aa3).T*.5))


dd= v(tab=Tr_i,tabv=Tr_i ,d=2,fv=35.,nu=7.0)
dd2=v(tab=Tr_i,tabv=D_i ,d=2,fv=35.,nu=7.0)

dd3=v(tab=Tr_i,tabv=Tr_i,d=2,fv=35.,nu=7.0)
dd4=v(tab=Tr_i,tabv=S_i ,d=2,fv=35.,nu=7.0)

dd5=v(tab=Tr_i,tabv=Q_i ,d=2,fv=35.,nu=7.0)
dd6=v(tab=Tr_i,tabv=S_i ,d=2,fv=35.,nu=7.0)

dd7=v(tab=Tr_i,tabv=Q_i ,d=2,fv=35.,nu=7.0)
dd8=v(tab=Tr_i,tabv=D_i ,d=2,fv=35.,nu=7.0)

zz=V((H((dd,dd3,dd5,dd7)), H((dd2,dd4,dd6,dd8))))
aa1=n.array(list(v(tabv=Q_i,fv=.5,f=200,nu=9))*4)
aa2=n.array(v(tabv=Tr_i,fv=.25/2.,f=200,nu=9,d=8.))
aa3=n.array(v(fv=.25/2.,f=200,nu=9,d=8.))

aa=n.vstack(( aa, (zz+aa1).T*.5, (zz+aa2).T*.5,(zz+aa3).T*.5))


dd= v(tab=Q_i,tabv=Tr_i ,d=2,fv=35.,nu=7.0)
dd2=v(tab=Q_i,tabv=D_i ,d=2,fv=35.,nu=7.0)

dd3=v(tab=Q_i,tabv=Tr_i,d=2,fv=35.,nu=7.0)
dd4=v(tab=Q_i,tabv=S_i ,d=2,fv=35.,nu=7.0)

dd5=v(tab=Q_i,tabv=Q_i ,d=2,fv=35.,nu=7.0)
dd6=v(tab=Q_i,tabv=S_i ,d=2,fv=35.,nu=7.0)

dd7=v(tab=Q_i,tabv=Q_i ,d=2,fv=35.,nu=7.0)
dd8=v(tab=Q_i,tabv=D_i ,d=2,fv=35.,nu=7.0)

zz=V((H((dd,dd3,dd5,dd7)), H((dd2,dd4,dd6,dd8))))
aa1=n.array(list(v(tabv=Q_i,fv=.5,f=200,nu=9))*4)
aa2=n.array(v(tabv=Tr_i,fv=.25/2.,f=200,nu=9,d=8.))
aa3=n.array(v(fv=.25/2.,f=200,nu=9,d=8.))

aa=n.vstack(( aa, (zz+aa1).T*.5, (zz+aa2).T*.5,(zz+aa3).T*.5))

dd= v(tab=D_i,tabv=Tr_i ,d=2,fv=35.,nu=7.0)
dd2=v(tab=D_i,tabv=D_i ,d=2,fv=35.,nu=7.0)

dd3=v(tab=D_i,tabv=Tr_i,d=2,fv=35.,nu=7.0)
dd4=v(tab=D_i,tabv=S_i ,d=2,fv=35.,nu=7.0)

dd5=v(tab=D_i,tabv=Q_i ,d=2,fv=35.,nu=7.0)
dd6=v(tab=D_i,tabv=S_i ,d=2,fv=35.,nu=7.0)

dd7=v(tab=D_i,tabv=Q_i ,d=2,fv=35.,nu=7.0)
dd8=v(tab=D_i,tabv=D_i ,d=2,fv=35.,nu=7.0)

zz=V((H((dd,dd3,dd5,dd7)), H((dd2,dd4,dd6,dd8))))
aa1=n.array(list(v(tabv=Q_i,fv=.5,f=200,nu=9))*4)
aa2=n.array(v(tabv=Tr_i,fv=.25/2.,f=200,nu=9,d=8.))
aa3=n.array(v(fv=.25/2.,f=200,nu=9,d=8.))

aa=n.vstack(( aa, (zz+aa1).T*.5, (zz+aa2).T*.5,(zz+aa3).T*.5))

print("BellaRugosiSdadE.wav escrito")
a.wavwrite(aa,"BellaRugosiSdadE.wav",f_a)
#a.wavwrite(aa,"BellaRugosidade.wav",f_a)

