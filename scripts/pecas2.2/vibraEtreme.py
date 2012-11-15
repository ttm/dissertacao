#-*- coding: utf8 -*-
import numpy as n, scikits.audiolab as a

# montagem dedicada a explorar tremolos e vibratos
# independentemente e combinados

# partes:

# 1) som senoidal, vibrato senoidal com
# varreduras de frequência e de profundidade
# com a portadora em ao menos 3 frequencias diferentes

# 2) variacoes de vibrato em escala log e lin

# 3) vibratos com padrões diferentes do senoidal, sons diferentes
# do senoidal

# 4), 5) e 6) análogos para tremolos

# 7) usos combinados de ambos.

# * Todas as etapas se estendem para AM e FM

###################################################
# PARTE 1)

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



