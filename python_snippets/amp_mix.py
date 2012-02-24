seq=[1.5*i for i in fazSequencia(nt, f, fator, d, s, senoide, dente)] # amplificacao

seq3=[(i+j) for i,j in zip(seq1,seq2)] # mixagem

seq2=somador(ac,seq2) # mixando igual acima, mas quando os comprimentos nao sao os mesmos