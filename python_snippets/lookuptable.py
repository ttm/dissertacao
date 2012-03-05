# fixados a frequencia (Hz), a duracao (segundos) e a tabela (1 ciclo da onda)
# e a taxa de amostragem (44,1kHz, 48kHz, 8kHz, etc)
# exemplo:
# freq = 200
# dur = .2 
# tabela = '1 ciclo de senoide ou outra forma de onda em 1024 amostras' 
T=len(tabela)
incremento=freq*T/taxa_amostragem
ap=0
amostras=[]
for i in xrange(int(dur*taxa_amostragem)):
    amostras.append(tabela[int(ap)])
    ap=incremento+ap
