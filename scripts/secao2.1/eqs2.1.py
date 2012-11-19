#-*- coding: utf8 -*-
import numpy as n, pylab as p, scikits.audiolab as a

############## 2.1.1 Duração
### 2.1
# a equação relaciona o número de amostras à duração do som
f_a=44100 # frequência de amostragem
Delta=3.7 # duração de 3.7 segundos

# som de duração 3.7 segundos => 3.7*44100 amostras
T_i=n.zeros(int(f_a*Delta)) # por hora fizemos silencio

# escrevendo em disco como arquivo PCM (WAV no caso)
a.wavwrite(T_i,"silencio.wav",f_a) 


############## 2.1.2 Volume
### 2.2
Lambda=100 # o som terá 100 amostras
T_i=n.random.random(Lambda) # 100 amostras quaisquer
pot=(T_i**2).sum()/Lambda #potência

### 2.3
T2_i=n.random.normal(size=Lambda)
pot2=(T2_i**2).sum()/Lambda #potência
V_dB=10*n.log10(pot2/pot)

### 2.6
A = 10**(V_dB/20)


############## 2.1.3 Altura
### 2.7
f_0=441
lambda_0=f_a/f_0
periodo=n.arcsin(n.random.random(lambda_0))
Tf_i=n.array(list(periodo)*100)
# normalizando para convencao no intervalo [-1,1]
Tf_i=((Tf_i-Tf_i.min())/(Tf_i.max()-Tf_i.min()))*2.-1. 
a.wavwrite(Tf_i,"f_0.wav",f_a) 


############## 2.1.4 Timbre
T=100000 # número de amostras para realizarmos as sequencias
ii=n.arange(T)
f=220.5
lambda_f=int(f_a/f)
### 2.8
Sf_i=n.sin(2*n.pi*f*ii/f_a)
### 2.9
Df_i=(2/lambda_f)*(ii*lambda_f)-1
### 2.10
Tf_i=1-n.abs(2-(4/lambda_f)*(ii%lambda_f))
### 2.11
Qf_i=((ii%lambda_f)<(lambda_f/2))*2-1

###2.12
r=a.wavread("22686__acclivity__oboe-a-440_periodo.wav")[0]
Tf_i=r[ii%len(r)]


############## 2.1.5 O espectro no som amostrado
Lambda=50
T_i=n.random.random(Lambda)*2-1
C_k=n.fft.fft(T_i)
A_k=n.real(C_k)
B_K=n.imag(C_k)
### 2.13
def t(i): 
    w_k=2*n.pi*n.arange(Lambda)/Lambda
    return (1./Lambda)*n.sum(C_i*n.e**(1j*w_k*i))
### 2.14
def t(i):
    w_k=2*n.pi*n.arange(Lambda)/Lambda
    return (1./Lambda)*n.sum(n.abs(C_k)*n.cos(w_k*i-n.angle(C_k)))
### 2.15
# numero de coeficientes espectrais pareados
tau = (Lambda - Lambda%2)/2 + Lambda%2-1
### 2.19
def t(i):
    w_k=2*n.pi*n.arange(Lambda)/Lambda
    return (1./Lambda)*(A_k[0]+2*n.sum(n.abs(C_k[1:tau+1])*\
            n.cos(w_k*i-n.angle(C_k)) + a[Lambda/2]*(1-Lambda%2)))


############## 2.1.6 Localização espacial
zeta=0.215 # metros
# tomemos localizacao (x,y) qualquer
x=1.5 # metros
y=1. #metros
### 2.20
d=n.sqrt(  (x-zeta/2)**2+y**2  )
d2=n.sqrt(  (x+zeta/2)**2+y**2  )
### 2.21
DTI=(d2-d)/343.2 # segundos
### 2.22
DII=20*n.log10(d/d2) # dBs
### 2.23
Lambda_DTI=int(DTI*f_a)
DII_a=d/d2
T_i=1-n.abs(2-(4./lambda_f)*(ii%lambda_f)) # triangular
T2_i = n.hstack((n.zeros(Lambda_DTI),DII_a*T_i))

T_i=n.hstack((T_i,n.zeros(Lambda_DTI)))

som=n.vstack((T2_i,T_i)).T
a.wavwrite(som,"estereo.wav",f_a)
# espelhando
som=n.vstack((T_i,T2_i)).T
a.wavwrite(som,"estereo2wav",f_a)


############## 2.1.7 A nota básica
### 2.27
f=220.5 # Herz 
Delta=2.5 # segundos
Lambda=int(2.5*f_a)
ii=n.arange(Lambda)
Lf_i=Df_i # Já fizemos acima
TfD_i=Lf_i[ii%len(Lf_i)]


############## 2.1.8 Usos musicais
Delta=3 # 3 segundos
Lambda=int(Delta*f_a)
f1=200. # Hz
foo=n.linspace(0,Delta*f1*2*n.pi,Lambda,endpoint=False)
T1_i=n.sin(foo) # senoide de Delta segundos e freq = f1

f2=245. # Hz
lambda_f2=int(f_a/f2)
T2_i=(n.arange(Lambda)%lambda_f<(lambda_f2/2))*2-1

f3=252. # Hz
lambda_f3=f_a/f3
T3_i=n.arange(Lambda)%lambda_f3
T3_i=(T3_i/T3_i.max())*2-1

### 2.28 mixagem
T_i=T1_i+T2_i+T3_i
# normalizando
T_i=((T_i-T_i.min())/(T_i.max()-T_i.min()))*2-1
# escrevendo arquivo
a.wavwrite(T_i,"mixados.wav",f_a)

### 2.29 concatenação
T_i=n.hstack((T1_i,T2_i,T3_i))
# escrevendo arquivo
a.wavwrite(T_i,"concatenados.wav",f_a)

