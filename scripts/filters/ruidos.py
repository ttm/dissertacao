#-*- coding: utf8 -*-
import numpy as n, pylab as p, scikits.audiolab as a

N = 100000 # N sempre par
fa=44100.
################
# geracao do ruido branco

# geracao de espectro com modulo 1 uniforme
# e fase aleatoria
coefs=n.exp(1j*n.random.uniform(0, 2*n.pi, N))

# real par, imaginaria impar
coefs[N/2+1:]=n.real(coefs[1:N/2])[::-1] - 1j*n.imag(coefs[1:N/2])[::-1]

coefs[0]=0. # sem bias
coefs[N/2]=0.9 # freq max eh real e 0.9

ruido=n.fft.ifft(coefs)
r=n.real(ruido)
r=((r-r.min())/(r.max()-r.min()))*2-1
a.wavwrite(r,'branco.wav',44100)

p.plot(n.real(ruido))
p.show()


################3
# Ruido rosa
df=fa/N
fi=n.arange(coefs.shape[0])*df
f0=15. # iniciamos o ruido em 15 Hz
i0=n.floor(f0/df) # primeiro coeff a valer
coefs[:i0]=n.zeros(i0)
f0=fi[i0]


# para cada oitava, perde 3dB, i.e. cai para ~0.707 da amplitude
fator=10.**(-3/20.)

alphai=fator**(n.log2(fi[i0:]/f0))

c=coefs[:]
c[i0:]=coefs[i0:]*alphai
# real par, imaginaria impar
c[N/2+1:]=n.real(c[1:N/2])[::-1] - 1j*n.imag(c[1:N/2])[::-1]

ruido=n.fft.ifft(c)
r=n.real(ruido)
r=((r-r.min())/(r.max()-r.min()))*2-1
a.wavwrite(r,'rosa.wav',44100)

p.plot(n.real(ruido))
p.show()


################3
# Ruido marrom
df=fa/N
fi=n.arange(coefs.shape[0])*df
f0=15. # iniciamos o ruido em 15 Hz
i0=n.floor(f0/df) # primeiro coeff a valer
coefs[:i0]=n.zeros(i0)
f0=fi[i0]


# para cada oitava, perde 6dB, i.e. cai para ~0.501 da amplitude
fator=10.**(-6/20.)

alphai=fator**(n.log2(fi[i0:]/f0))
c=coefs[:]
c[i0:]=coefs[i0:]*alphai
# real par, imaginaria impar


c[N/2+1:]=n.real(c[1:N/2])[::-1] - 1j*n.imag(c[1:N/2])[::-1]

ruido=n.fft.ifft(c)
r=n.real(ruido)
r=((r-r.min())/(r.max()-r.min()))*2-1
a.wavwrite(r,'marrom.wav',44100)

p.plot(n.real(ruido))
p.show()









