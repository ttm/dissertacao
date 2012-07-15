# Note as variáveis que são fixadas de antemão
def fazSequencia(notas, f0, fator, dur_nota, dur_silencio,
                                        funcao1, funcao2=0):
    seq=[] # a sequência é iniciada vazia
    for nota in notas: # para cada nota
        # a frequência é a fundamental vezes 2
        # elevado ao número de semitons:
        freq=f0*fator**nota
        if funcao2: # caso a funcao2 seja especificada
            # fazer o waveshaping:
            amostras=lookupcruz(funcao1,funcao2,dur_nota,freq)
        else:
            # ou faz com a forma de onda simples:
            amostras=lookup(funcao1,dur_nota,freq)
        # soma o silêncio
        amostras += [0]*int(taxa_amostragem*dur_silencio)
        seq += amostras # concatena na sequência principal
    # normalização em 2 passos:
    smin=min(seq); smax=max(seq)
    seq= [(-.5+(i-smin)/(smax-smin)) for i in seq]
    return seq # retorna a sequência pronta
