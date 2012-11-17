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
    Lv=float(len(S_i))

    Gammav_i=n.floor(ii*fv*Lv/f_a) # índices para a LUT
    Gammav_i=n.array(Gammav_i,n.int)
    Tv_i=tabv[Gammav_i%int(Lv)] # padrão de variação do vibrato para cada amostra

    F_i=f*(   2.**(  Tv_i*nu/12.  )   ) # frequência em Hz em cada amostra

    D_gamma_i=F_i*(Lt/float(f_a)) # a movimentação na tabela por amostra
    Gamma_i=n.cumsum(D_gamma_i) # a movimentação na tabela total
    Gamma_i=n.floor( Gamma_i) # já os índices
    Gamma_i=n.array( Gamma_i, dtype=n.int) # já os índices
    return tab[Gamma_i%int(Lt)] # busca dos índices na tabela

def A(fa=2.,V_dB=10.,d=2.,taba=S_i):
    Lambda=n.floor(f_a*d)
    ii=n.arange(Lambda)
    Lt=float(len(taba))
    Gammaa_i=n.floor(ii*fa*Lt/f_a) # índices para a LUT
    Gammaa_i=n.array(Gammaa_i,n.int)
### 2.55 padrão de oscilação do vibrato
    A_i=taba[Gammaa_i%int(Lt)] # padrão de variação da amplitude do tremolo para cada amostra
    A_i=A_i*10.**(V_dB/20.)
    return A_i


def adsr(som,A=10.,D=20.,S=-20.,R=100.,xi=1e-2):
    a_S=10**(S/20.)
    Lambda=len(som)
    Lambda_A=int(A*f_a*0.001)
    Lambda_D=int(D*f_a*0.001)
    Lambda_R=int(R*f_a*0.001)

    ii=n.arange(Lambda_A,dtype=n.float)
    A=ii/(Lambda_A-1)
    A_i=A
    ii=n.arange(Lambda_A,Lambda_D+Lambda_A,dtype=n.float)
    D=1-(1-a_S)*(   ( ii-Lambda_A )/( Lambda_D-1) )
    A_i=n.hstack(  (A_i, D  )   )
    S=n.ones(Lambda-Lambda_R-(Lambda_A+Lambda_D),dtype=n.float)*a_S
    A_i=n.hstack( ( A_i, S )  )
    ii=n.arange(Lambda-Lambda_R,Lambda,dtype=n.float)
    R=a_S-a_S*((ii-(Lambda-Lambda_R))/(Lambda_R-1))
    A_i=n.hstack(  (A_i,R)  )

    return som*A_i


s=v(f=200.,nu=0.)
s0=n.copy(s)
amb=2**(.1/12.)
f=200.
amb=2**(.00/12.)*f
amb_trem=.5
for i in xrange(10):
    f_=f+amb*n.random.random()-amb/2.
    s+=v(f=f_,nu=n.random.random()*amb_trem-amb_trem/2)

T_i=n.hstack((s0,s))

T_i=((T_i-T_i.min())/(T_i.max()-T_i.min()))*2-1
        
a.wavwrite(T_i,"chorusInfantil.wav",f_a) # escrita do som




######################
s=v(f=200.,nu=0.)
s0=n.copy(s)

amb=.1 # semitons
f=200.
amb_vib=.5
amb_ft=.4
for i in xrange(10):
    f_=f*2.**((n.random.random()-.5)*amb/12.)
    nu_=(n.random.random()-.5)*amb_vib
    s+=v(   f=f_,   nu=nu_    )

T_i=n.hstack((s0,s))


s=v(f=200.,nu=0.)
s0=n.copy(s)
amb=2**(.01/12.)
f=200.
amb=2**(.00/12.)*f
amb_trem=.5
for i in xrange(10):
    f_=f+amb*n.random.random()-amb/2.
    s+=v(  f_,   nu=n.random.random()*amb_trem-amb_trem/2.    )

T_i=n.hstack((T_i,s0,s))

s=v(f=200.,nu=0.)
s0=n.copy(s)
amb=2**(.01/12.)
f=200.
amb=2**(.00/12.)*f
amb_trem=.1
for i in xrange(10):
    s+=v(   f=200.*(n.random.random()*amb-amb/2.),   nu=n.random.random()*amb_trem-amb_trem/2.    )

T_i=n.hstack((T_i,s0,s))

s=v(f=200.,nu=0.)
s0=n.copy(s)
amb=2**(.01/12.)
f=200.
amb=2**(.00/12.)*f
amb_trem=.0
for i in xrange(10):
    s+=v(   f=200.*(n.random.random()*amb-amb/2.),   nu=n.random.random()*amb_trem-amb_trem/2.    )

T_i=n.hstack((T_i,s0,s))

s=v(f=200.,nu=0.)
s0=n.copy(s)
f=200.
amb=2**(.00/12.)*f
f=200.
amb=2**(.00/12.)*f
amb_trem=.0
for i in xrange(10):
    f_=f+amb*n.random.random()-amb/2.
    s+=v(   f=f_,   nu=n.random.random()*amb_trem-amb_trem/2.    )

T_i=n.hstack((T_i,s0,s))


T_i=((T_i-T_i.min())/(T_i.max()-T_i.min()))*2-1
        
a.wavwrite(T_i,"chorusInfantil3.wav",f_a) # escrita do som


