# inicializamos as variáveis:
notas=[1,4,5,6,7]
fundamental=200
fator=2**(1/12.)
dur_nota=0.5
dur_silencio=0.1
onda1=senoide
onda2=dente_de_serra
# realização da sequência com senóides:
sequencia = fazSequencia( notas,
                          fundamental, 
                          fator, 
                          dur_nota, 
                          dur_silencio, 
                          onda1 ) 
# realização do acorde com waveshaping
acorde = fazAcorde( notas
                    fundamental,
                    fator,
                    dur_nota,
                    dur_silencio,
                    onda1,
                    onda2 )
