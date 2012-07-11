import numpy as n # utilizamos o numpy aqui por simplicidade
T=1024 # tamanho suficiente para a lookup, como mencionado acima

foo=n.linspace(0,2*n.pi,T,endpoint=False) # de 0 até 2*pi em T amostras
senoide=n.sin(foo) # seno de foo dá um ciclo de senóide

dente_de_serra=n.linspace(-1,1,T,endpoint=False)
triangular=n.hstack((dente[::2],dente[-1:0:-2]))
quadrada=n.hstack((n.ones(T/2),n.ones(T/2)*-1))
