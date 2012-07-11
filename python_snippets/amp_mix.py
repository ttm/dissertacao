#-# De posse das notas, fundamental, fator, durações e ondas #-#
# sequência do restrogrado das notas com waveshapping:
sequencia1 = fazSequencia(nt[::-1], f, fator, d, s, senoide, dente)
# sequência original das notas uma quinta justa acima,
# com dente de serra:
sequencia2 = fazSequencia(nt, f*(3/2.), fator, d, s, dente)

#-# Procedimentos básicos #-#
# concatenação
seq = sequencia1+sequencia2 
# amplificação e concatenação
seq += [1.5*i for i in sequencia1] 
# mixagem e concatenação
seq += [(i+j) for i,j in zip(sequencia1,sequencia2)] 
# mixando igual acima, mas quando os comprimentos
# dos vetores não são os mesmos
seq += somador(seq,sequencia2) 
