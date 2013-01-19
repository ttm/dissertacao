#_8_ coding: utf8 -*-
import numpy as n

f_a = 44100.  # Hz, frequência de amostragem
Lambda_tilde = Lt = 1024.
foo = n.linspace(0, 2*n.pi, Lt, endpoint=False)
S_i = n.sin(foo)  # um período da senóide com T amostras


def v(f=200, d=2., tab=S_i, fv=2., nu=2., tabv=S_i):
    Lambda = n.floor(f_a*d)
    ii = n.arange(Lambda)
    Lv = float(len(S_i))

    Gammav_i = n.floor(ii*fv*Lv/f_a)  # índices para a LUT
    Gammav_i = n.array(Gammav_i, n.int)
    # padrão de variação do vibrato para cada amostra
    Tv_i = tabv[Gammav_i % int(Lv)]

    # frequência em Hz em cada amostra
    F_i = f*(2.**(Tv_i*nu/12.))
    # a movimentação na tabela por amostra
    D_gamma_i = F_i*(Lt/float(f_a))
    Gamma_i = n.cumsum(D_gamma_i)  # a movimentação na tabela total
    Gamma_i = n.floor(Gamma_i)  # já os índices
    Gamma_i = n.array(Gamma_i, dtype=n.int)  # já os índices
    return tab[Gamma_i % int(Lt)]  # busca dos índices na tabela


############## 2.3.1 Afinação, intervalos, escalas e acordes

### 2.76 Intervalos
I1j = 0.
I2m = 1.
I2M = 2.
I3m = 3.
I3M = 4.
I4J = 5.
ITR = 6.
I5J = 7.
I6m = 8.
I6M = 9.
I7m = 10.
I7M = 11.
I8J = 12.
I_i = n.arange(13.)


# o intervalo soma nove nomenclatuda da inversão
# mas soma sempre 12 na inversão de semitons
def inv(I):
    """retorna intervalo inverso de I: 0< =  I < = 12"""
    return 12-I


# intervalo harmonico
def intervaloHarmonico(f, I):
    return (v(f)+v(f*2.**(I/12.)))*0.5


# intervalo melódico
def intervaloMelodico(f, I):
    return n.hstack((v(f), v(f*2.**(I/12.))))

### 2.77 Escalas simétricas
Ec_i = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11.]
Et_i = [0., 2., 4., 6., 8., 10.]
Etm_i = [0., 3., 6., 9.]
EtM_i = [0., 4., 8.]
Ett_i = [0., 6.]

### 2.78 Escalas diatônicas
Em_i = [0., 2., 3., 5., 7., 8., 10.]
Emlo_i = [1., 3., 5., 6., 8., 10.]
EM_i = [0., 2., 4., 5., 7., 9., 11.]
Emd_i = [0., 2., 3., 5., 7., 9., 10.]
Emf_i = [0., 1., 3., 5., 7., 8., 10.]
Eml_i = [0., 2., 4., 6., 7., 9., 11.]
Emmi_i = [0., 2., 4., 5., 7., 8., 10.]

### 2.79 Padrão diatônico
E_i_ = n.roll(n.array([2.,2.,1.,2.,2.,2.,1.]), n.random.randint(7.))
E_i = n.cumsum(E_i_)-E_i_[0.]


### 2.80 Escalas menores harmônica e melódica
Em_i = [0., 2., 3., 5., 7., 8., 10.]
Emh_i = [0., 2., 3., 5., 7., 8., 11.]
Emm_i = [0.,2.,3.,5.,7.,9.,11.,12.,10.,8.,7.,5.,3.,2.,0.]


### 2.81 Tríades
AM_i = [0., 4., 7.]
Am_i = [0., 3., 7.]
Ad_i = [0., 3., 6.]
Aa_i = [0., 4., 8.]

def comSetimam(A): return A+[10.]
def comSetimaM(A): return A+[11.]

### Microtonalidade de quartos de tom
### e sétimos de oitava
# com
epslon = 2**(1/12.)
s1 = [0., 0.25, 1.75, 2., 2.25, 4., 5., 5.25]
#ou
epslon = 2**(1/7.)
s2 = [0., 1., 2., 3., 4., 5., 6.]


############## 2.3.2 Rudimentos de harmonia
### Figura 2.22
def relativa(TT):
    """TT é tríade maior ou menor em posicão fechada e fundamental"""
    T = n.copy(TT)
    if T[1]-T[0] == 4.:  # ac maior
        T[2] = 9.  # retorna acorde menor abaixo
    elif T[1]-T[0] == 3.:  # ac menor
        T[0] = 10.  # retorna acorde maior acima
    else:
        print("send me only minor or major perfect triads")
    return T


def antiRelativa(TT):
    T = n.copy(TT)
    if T[1]-T[0] == 4.:  # maior
        T[0] = 11.  # retorna menor acima
    if T[1]-T[0] == 3.:  # menor
        T[2] = 8.  # retorna maior abaixo
    return T


class Mediana:
    def sup(self, TT):
        T = n.copy(TT)
        if T[1]-T[0] == 4.:  # maior
            T[0] = 11.
            T[2] = 8.  # retorna maior
        if T[1]-T[0] == 3.:  # menor
            T[0] = 10.
            T[2] -= 1.  # retorna menor
        return T

    def inf(self, TT):
        T = n.copy(TT)
        if T[1]-T[0] == 4.:  # maior
            T[2] = 9
            T[0] = 1.  # retorna maior
        if T[1]-T[0] == 3.:  # menor
            T[2] = 8.
            T[0] = 11.  # retorna menor
        return T

    def supD(self, TT):
        """Preserva a quinta da primeira tríade na terça """
        T = n.copy(TT)
        if T[1]-T[0] == 4.:  # maior
            T[0] = 10.
            T[1] = 3.  # retorna maior
        if T[1]-T[0] == 3.:  # menor
            T[0] = 11.
            T[1] = 4.  # retorna menor
        return T

    def infD(self, TT):
        T = n.copy(TT)
        if T[1]-T[0] == 4.:  # maior
            T[1] = 3.
            T[2] = 8.  # retorna maior
        if T[1]-T[0] == 3.:  # menor
            T[1] = 4.
            T[2] = 9.  # retorna menor
        return T

### Tônicas e funções principais
tonicaM = [0., 4., 7.]
tonicam = [0., 3., 7.]
subM = [0., 5., 9.]
subm = [0., 5., 8.]
dom = [2., 7., 11.]
Vm = [2., 7., 10.]  # quinto grau menor nao eh dominante


############## 2.3.3 Contraponto

def contraNotaNotaSup(alturas=[0,2,4,5,5,0,2,0,2,2,2,0,7,
                        5,4,4,4,0,2,4,5,5,5]):
    """Realiza rotina de independência das vozes

    Limitado em 1 oitava acima da nota"""
    primeiraNota = alturas[0]+(7, 12)[n.random.randint(2)]
    contra = [primeiraNota]

    i = 0
    cont = 0  # contador de paralelas
    for al in alturas[:-1]:
        mov_cf = alturas[i:i+2]
        atual_cf, seguinte_cf = mov_cf
        if seguinte_cf-atual_cf > 0:
            mov = "asc"
        elif seguinte_cf-atual_cf < 0:
            mov = "asc"
        else:
            mov = "obl"

        # possibilidades por consonancia
        possiveis = [seguinte_cf+interval for interval in
                                    [0,3,4,5,7,8,9,12]]
        movs = []
        for pos in possiveis:
            if pos - contra[i] < 0:
                movs.append("desc")
            if pos - contra[i] > 0:
                movs.append("asc")
            else:
                movs.append("obl")

        movt = []
        for m in movs:
            if 'obl' in (m, mov):
                movt.append("obl")
            elif m == mov:
                movt.append("direto")
            else:
                movt.append("contrario")
        for nota, mt in zip(possiveis, movt):

            if mt == "direto":  # mov direto
                # n aceita intervalo perfeito
                if nota-seguinte_cf in (0,7,8,12):
                    possiveis.remove(nota)
        ok = 0
        while not ok:
            nnota = possiveis[n.random.randint(len(possiveis))]
            if nnota-seguinte_cf == contra[i]-atual_cf:  # paralelo
                intervalo = contra[i]-atual_cf
                novo_intervalo = nnota-seguinte_cf
                # do mesmo tipo 3 ou 6
                if abs(intervalo-novo_intervalo) == 1:
                    if cont == 2:  # se já teve 2 paralelas
                        pass  # outro intrevalo
                    else:
                        cont += 1
                        ok = 1
            else:  # mov obl ou contrario
                cont = 0  # zera paralelos
                ok = 1
        contra.append(nnota)
        i += 1
    return contra



############## 2.3.4 Ritmo
### Veja peça Poli Hit Mia no Apêndice B


############## 2.3.5 Estruturas direcionais
### Veja peça Dirracional no Apêndice B


############## 2.3.6 Estruturas cíclicas
### Veja as peças 3 Trios no Apêndice B
### e o PPEPPS no Apêndice C
