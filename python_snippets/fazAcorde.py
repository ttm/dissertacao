def fazAcorde(notas, f0, fator, dur_nota, dur_silencio, funcao1, funcao2=0):
    seq=[]
    for nota in notas:
        freq=f0*fator**nota
        if funcao2:
            amostras=lookupcruz(funcao1,funcao2,dur_nota,freq)
        else:
            amostras=lookup(funcao1,dur_nota,freq)
        amostras=amostras+[0]*int(dur_silencio*taxa_amostragem)
        # para sobrepor unidades de tamanhos diferentes
        # é conveniente uma função auxiliar
        seq=somador(seq,amostras) 
    # normalizaçào em duas linhas:
    smin=min(seq); smax=max(seq)
    seq= [(-.5+(i-smin)/(smax-smin)) for i in seq]
    return seq
