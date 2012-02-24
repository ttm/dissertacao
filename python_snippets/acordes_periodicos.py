ac=[]
for i in xrange(8): # a cada 2 tempos
    ac+=fazAcorde([0,7,14,21,28,35,42,49,56,63,70,77,84], f, fator, d, s, senoide, dente)
    ac+=[0]*int((d+s)*44100)