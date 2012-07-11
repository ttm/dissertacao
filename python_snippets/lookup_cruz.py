# T, incremento, n_amostras e dur definidos como no script anterior
ap=0.0
amostras=[0] * n_amostras 
for i in xrange(n_amostras): # n_de_amostras = dur * 44100
    foo=func[int(ap)] # foo entre [-1,1]
    bar=( bar + (T/2) )*(T/2) # centrando no meio da tabela e ampliando o âmbito 
    amostras[i] = func2[int(bar)]
    ap = (SI + ap)%T

