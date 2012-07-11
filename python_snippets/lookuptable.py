# -*- coding: utf-8 -*-
# fixados a duração (segundos) e a taxa de amostragem (amostras por segundo),
# temos o número de mostras da unidade a ser sintetizada:
dur = 2.0 # 2 segundos
taxa_amostragem = 44100 # 44.1kHz, padrão de Compact Disk e outras mídias 

n_amostras = int(dur * taxa_amostragem)

# fixadas também a frequencia (Hz), e a tabela (1 ciclo da onda):
freq = 220 # 220 Hz, Lá 3
# tabela = 1 ciclo de senoide ou outra forma de onda em 1024 amostras, ver abaixo para diferentes tabelas

# O procedimento de lookup table é relativamente simples.
# Mesmo assim, depende de uma pequena dedução, feita a seguir:
T=len(tabela) # tamanho da tabela, i.e. número de amostras da tabela, i.e. número de amostras em um ciclo

# Note que:
# taxa_amostragem ≡ amostras / segundo
# freq ≡ ciclos / segundo
# ∴ taxa_amostragem / freq ≡ amostras / ciclo

# Neste ponto, basta perceber que a tabela
# usada para lookup também possui um número de
# amostras para cada ciclo e que a proporção
# entre o número de amostras dela e o número
# de amostras na frequência desejada (e na taxa de
# amostragem utilizada) dá o incremento entre diferentes
# amostras:
# T / (taxa_amostragem / freq) ≡

incremento=freq*T/taxa_amostragem # velocidade de leitura da tabela

ap=0.0 # apontador para manter a trilha da posição correta na tabela
amostras=[0] * n_amostras # vetor de zeros com o tamanho do vetor final
for i in xrange(n_amostras):
    amostras[i] = tabela[int(ap)]
    ap += incremento
