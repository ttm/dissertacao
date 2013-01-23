#-*- coding: utf8 -*-
import numpy as n
import scikits.audiolab as a

############## 2.1.1 Duração
# a equação relaciona o número de amostras à duração do som
f_a = 44100.  # frequência de amostragem
Delta = 3.7  # duração de Delta segundos  = >

Lambda = int(f_a*Delta)  # número de amostras
### 2.1
T_i = n.zeros(Lambda)  # silêncio com ~ Delta segundos

# escrita em disco como arquivo PCM (WAV no caso)
a.wavwrite(T_i, "silencio.wav", f_a)

############## 2.1.2 Volume
Lambda = 100.  # 100 amostras
T_i = n.random.random(Lambda)  # 100 amostras quaisquer

### 2.2  Potência
pot = (T_i**2.).sum()/Lambda

T2_i = n.random.normal(size=Lambda)
pot2 = (T2_i**2.).sum()/Lambda  # potência 2
### 2.3 Diferença de volume em decibels, dadas as potências
V_dB = 10.*n.log10(pot2/pot)

### 2.4 dobra amplitude  = > ganha 6 dB
T2_i = 2.*T_i
pot = (T_i**2.).sum()/Lambda  # potência
pot2 = (T2_i**2.).sum()/Lambda  # potência 2
V_dB = 10.*n.log10(pot2/pot)
Mm6 = abs(V_dB - 6) < .5  # Mm6 é True

### 2.5 dobra potência  = > ganha 3 dB
pot2 = 2.*pot
V_dB = 10.*n.log10(pot2/pot)
Mm3 = abs(V_dB - 3) < .5  # Mm3 é True

### 2.7 dobra volume  = > + 10 dB  = > aplitude * 3.16
V_dB = 10.
A = 10.**(V_dB/20.)
T2_i = A*T_i  # A ~ 3.1622776601

### 2.8 Conversão de decibels em amplificação
A = 10.**(V_dB/20.)


############## 2.1.3 Altura
f_0 = 441.
lambda_0 = f_a/f_0
periodo = n.arcsin(n.random.random(lambda_0))  # amostras quaisquer
### 2.9 Som com frequência fundamental f_0
Tf_i = n.array(list(periodo)*1000)  # 1000 períodos

# normalizando para convenção no intervalo [-1,1]
Tf_i = ((Tf_i-Tf_i.min())/(Tf_i.max()-Tf_i.min()))*2.-1.
a.wavwrite(Tf_i, "f_0.wav", f_a)  # escrita em disco


############## 2.1.4 Timbre
T = 100000.  # número de amostras das sequencias
ii = n.arange(T)
f = 220.5
lambda_f = f_a/f
### 2.10 Senoide
Sf_i = n.sin(2.*n.pi*f*ii/f_a)
### 2.11 Dente de serra
Df_i = (2./lambda_f)*(ii % lambda_f)-1
### 2.12 Triangular
Tf_i = 1.-n.abs(2.-(4./lambda_f)*(ii % lambda_f))
### 2.13 Onda quadrada
Qf_i = ((ii % lambda_f) < (lambda_f/2))*2-1

Rf_i = a.wavread("22686__acclivity__oboe-a-440_periodo.wav")[0]
### 2.14 Período amostrado
Tf_i = Rf_i[n.int64(ii) % len(Rf_i)]


############## 2.1.5 O espectro no som amostrado
Lambda = 50.
T_i = n.random.random(Lambda)*2.-1.
C_k = n.fft.fft(T_i)
A_k = n.real(C_k)
B_K = n.imag(C_k)
w_k = 2.*n.pi*n.arange(Lambda)/Lambda


### 2.15 Recomposição do espectro no tempo
def t(i):
    return (1./Lambda)*n.sum(C_k*n.e**(1j*w_k*i))


### 2.16 Recomposição real
def tR(i):
    return (1./Lambda)*n.sum(n.abs(C_k)*n.cos(w_k*i-n.angle(C_k)))

### 2.17 Número de coeficientes espectrais pareados
tau = (Lambda - Lambda % 2)/2 + Lambda % 2-1
### 2.18 Coeficientes equivalentes
kk = n.arange(tau)
F_k = C_k[1:tau+1]
F2_k = C_k[Lambda-tau:Lambda-1][::-1]

### 2.19 Coeficientes equivalentes: módulos
ab = n.abs(F_k)
ab2 = n.abs(F2_k)
MIN = n.abs(ab-ab2).sum()  # MIN ~ 0.0
### 2.20 Coeficientes equivalentes: fases
an = n.angle(F_k)
an2 = n.angle(F2_k)
MIN = n.abs(an+an2).sum()  # MIN ~ 0.0

### 2.21 Combinação das componentes em cada amostra
w_k = 2*n.pi*n.arange(Lambda)/Lambda


def t_(i):
    return (1./Lambda)*(A_k[0]+2.*n.sum(n.abs(C_k[1:tau+1]) *
                        n.cos(w_k*i-n.angle(C_k)) + a[Lambda/2] *
                        (1-Lambda % 2)))


############## 2.1.6 A nota básica
f = 220.5  # Herz
Delta = 2.5  # segundos
Lambda = int(2.5*f_a)
ii = n.arange(Lambda)
Lf_i = Df_i  # Já fizemos Df_i acima
### 2.24 Nota Básica
TfD_i = Lf_i[ii % len(Lf_i)]


############## 2.1.7 Localização espacial
zeta = 0.215  # metros
# tomemos localizacao (x,y) qualquer
x = 1.5  # metros
y = 1.  # metros
### 2.25 distâncias de cada ouvido
d = n.sqrt((x-zeta/2)**2+y**2)
d2 = n.sqrt((x+zeta/2)**2+y**2)
### 2.26 Distância de Tempo Interaural
DTI = (d2-d)/343.2  # segundos
### 2.27 Distância de Intensidade Interaural
DII = 20*n.log10(d/d2)  # dBs

### 2.28 aplicação de DTI e DII em T_i
Lambda_DTI = int(DTI*f_a)
DII_a = d/d2
T_i = 1-n.abs(2-(4./lambda_f)*(ii % lambda_f))  # triangular
T2_i = n.hstack((n.zeros(Lambda_DTI), DII_a*T_i))
T_i = n.hstack((T_i, n.zeros(Lambda_DTI)))

som = n.vstack((T2_i, T_i)).T
a.wavwrite(som, "estereo.wav", f_a)
# espelhando
som = n.vstack((T_i, T2_i)).T
a.wavwrite(som, "estereo2wav", f_a)

### 2.29 ângulo do objeto
theta = n.arctan(y/x)


############## 2.1.8 Usos musicais
Delta = 3.  # 3 segundos
Lambda = int(Delta*f_a)
f1 = 200.  # Hz
foo = n.linspace(0., Delta*f1*2.*n.pi, Lambda, endpoint=False)
T1_i = n.sin(foo)  # senoide de Delta segundos e freq  =  f1

f2 = 245.  # Hz
lambda_f2 = int(f_a/f2)
T2_i = (n.arange(Lambda) % lambda_f < (lambda_f2/2))*2-1  # quadrada

f3 = 252.  # Hz
lambda_f3 = f_a/f3
T3_i = n.arange(Lambda) % lambda_f3  # Dente de serra
T3_i = (T3_i/T3_i.max())*2-1

### 2.30 mixagem
T_i = T1_i+T2_i+T3_i
# normalização
T_i = ((T_i-T_i.min())/(T_i.max()-T_i.min()))*2-1
# escrita em disco
a.wavwrite(T_i, "mixados.wav", f_a)

### 2.31 concatenação
T_i = n.hstack((T1_i, T2_i, T3_i))
# escrita em disco
a.wavwrite(T_i, "concatenados.wav", f_a)
