# aproveitando a variavel
# acorde do script anterior
dur = dur_nota + dur_silencio
silencio_1_tempo = [0]*int((dur)*taxa_amostragem)

# adicionando o acorde a cada 2 tempos 8 vezes
# ou seja, por 16 tempos, durante 4 compassos de 4
# a música terá o acorde sedo tocado a cada 2 tempos:
ac += (acorde+silencio_1_tempo)*8
