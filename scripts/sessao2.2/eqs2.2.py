#-*- coding: utf8 -*-
import numpy as n, scikits.audiolab as a

f_a = 44100 # Hz, frequência de amostragem

############## 2.2.1 Tabela de Busca (LUT)
# tamanho da tabela: use par para não cnflitar abaixo
# e ao menos 1024
Lambda_tilde=Lt=1024

# Senóide
foo=n.linspace(0,2*n.pi,Lt,endpoint=False)
S_i=n.sin(foo) # um período da senóide com T amostras

# Quadrada:
Q_i=n.hstack(  ( n.ones(Lt/2)*-1 , n.ones(Lt/2) )  )

# Triangular:
foo=n.linspace(-1,1,Lt/2,endpoint=False)
T_i=n.hstack(  ( foo , foo*-1 )   )

# Dente de Serra:
D_i=n.linspace(-1,1,Lt)

# som real, importar período e
# usar T correto: o número de amostras do período

### 2.30
f=110. # Hz
Delta=3.4 # segundos
Lambda=int(Delta*f_a)

# Amostras:
I=n.arange(Lambda)
Gamma_i=n.array(I*f*Lt/f_a,dtype=n.int)

L_i=T_i # podemos usar igualmente S_i, Q_i, D_i ou qualquer

TfD_i=L_i[Gamma_i%Lt]







