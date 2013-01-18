#-*- coding: utf8 -*-
import numpy as n, pylab as p

ax=p.subplot(111)
p.xlabel(r"tempo $\rightarrow$",fontsize=19)
p.ylabel(r"amplitude $\rightarrow$", fontsize=19)

De=2*100. #duracao total (\Delta)
DA=2*20. # duracao do ataque \Delta_A
DD=2*20. # duracao do decay \Delta_D
DR=2*20. # duracao do release \Delta_R
SS=.4 # fração da amplitude em que ocorre o sustain
xi=1e-2 # -180dB para iniciar o fade in e finalizar o fade out

# Variações logarítmicas
#A=xi*(1./xi)**(n.arange(DA)/(DA-1)) # amostras do ataque
#s=n.copy(A) 
#D=SS**((n.arange(DA,DA+DD)-DA)/(DD-1)) # amostras do decay
#s=n.hstack((  s,  D  ))
#S=SS*n.ones(De-DR-(DA+DD)) # amostras do sustain
#s=n.hstack((  s, S  ))
#R=(SS)*(xi/SS)**(  (n.arange(De-DR,De)+DR-De)/(DR-1)  ) # amostras do release
#s=n.hstack((  s,  R  ))

A=n.arange(DA)/(DA-1) # amostras do ataque
s=n.copy(A) 
D=1-(1-SS)*((n.arange(DA,DA+DD)-DA)/(DD-1)) # amostras do decay
s=n.hstack((  s,  D  ))
S=SS*n.ones(De-DR-(DA+DD)) # amostras do sustain
s=n.hstack((  s, S  ))
R=SS-(SS)*(  (n.arange(De-DR,De)+DR-De)/(DR-1)  ) # amostras do release
s=n.hstack((  s,  R  ))


p.plot(A,                      'bo', markersize=4)
p.plot(n.arange(DA,DA+DD),D,   'go', markersize=4)
p.plot(n.arange(DA+DD,De-DR),S,'ko', markersize=4)
p.plot(n.arange(De-DR,De),R,   'ro', markersize=4)

p.text(2*6 ,.7,"A",fontsize=48,color='blue')
p.text(2*32,.7,"D",fontsize=48,color='green')
p.text(2*56,.5,"S",fontsize=48,color='black')
p.text(2*91,.3,"R",fontsize=48,color='red')

som=n.random.random(De)*2-1
som=n.sin(n.linspace(0,45*2*n.pi,De,endpoint=False))
som=som*s
p.plot(som,'c*',markersize=9,label=u"Som amostrado submetido à envoltória ADSR com variação linear")
p.plot(som,'c')
p.plot((len(som),len(som)),(-.8,0),"k--")

p.legend(loc="upper right",prop={'size':16})
p.xlim(-10,De+10)
p.ylim(-1.2,1.2)

p.yticks((-1,0,SS,1),(-1,0,r"$a_S$",1),fontsize=26)
p.xticks((len(som),),(r"$\Lambda$",),fontsize=26)

p.plot((-20,7),(SS,SS),'k--')
###############################
######################

De=2*100. #duracao total (\Delta)
DA=2*20. # duracao do ataque \Delta_A
DD=2*20. # duracao do decay \Delta_D
DR=2*20. # duracao do release \Delta_R
SS=.4 # fração da amplitude em que ocorre o sustain
xi=1e-2 # -180dB para iniciar o fade in e finalizar o fade out

# Variações logarítmicas
A=xi*(1./xi)**(n.arange(DA)/(DA-1)) # amostras do ataque
s=n.copy(A) 
D=SS**((n.arange(DA,DA+DD)-DA)/(DD-1)) # amostras do decay
s=n.hstack((  s,  D  ))
S=SS*n.ones(De-DR-(DA+DD)) # amostras do sustain
s=n.hstack((  s, S  ))
R=(SS)*(xi/SS)**(  (n.arange(De-DR,De)+DR-De)/(DR-1)  ) # amostras do release
s=n.hstack((  s,  R  ))

#A=n.arange(DA)/(DA-1) # amostras do ataque
#s=n.copy(A) 
#D=1-(1-SS)*((n.arange(DA,DA+DD)-DA)/(DD-1)) # amostras do decay
#s=n.hstack((  s,  D  ))
#S=SS*n.ones(De-DR-(DA+DD)) # amostras do sustain
#s=n.hstack((  s, S  ))
#R=SS-(SS)*(  (n.arange(De-DR,De)+DR-De)/(DR-1)  ) # amostras do release
#s=n.hstack((  s,  R  ))


p.plot(                      A-2.5,                      'bo', markersize=4)
p.plot(n.arange(DA,DA+DD),   D-2.5,   'go', markersize=4)
p.plot(n.arange(DA+DD,De-DR),S-2.5,'ko', markersize=4)
p.plot(n.arange(De-DR,De),   R-2.5,   'ro', markersize=4)

som=n.random.random(De)*2-1
som=n.sin(n.linspace(0,45*2*n.pi,De,endpoint=False))
som=som*s
p.plot(som-2.5,'md',markersize=9,label=u"Som amostrado submetido à envoltória ADSR com variação logarítmica")
p.plot(som-2.5,'m')
p.plot((len(som),len(som)),(-.8-2.5,0-2.5),"k--")

p.legend(loc="upper right",prop={'size':16})
p.xlim(-10,De+10)
p.ylim(-3.8,1.8)

p.yticks((-1,0,SS,1),(-1,0,r"$a_S$",1),fontsize=26)
p.xticks((len(som),),(r"$\Lambda$",),fontsize=26)


p.arrow(0,    -1.1-2.5,DA,0,length_includes_head=True,shape='full',head_width=.1,color='cyan'     ,width=0.009)
p.arrow(DA,   -1.1-2.5,-DA,0,length_includes_head=True,shape='full',head_width=.1,color='blue'   ,width=0.009)  
p.arrow(DA+DD,-1.1-2.5,-DD,0,length_includes_head=True,shape='full',head_width=.1,color='cyan',width=0.009)
p.arrow(DA,   -1.1-2.5,DD,0,length_includes_head=True,shape='full',head_width=.1,color='green'   ,width=0.009)
p.arrow(De,   -1.1-2.5,-DR,0,length_includes_head=True,shape='full',head_width=.1,color='red'    ,width=0.009)
p.arrow(De-DR,-1.1-2.5,DR,0,length_includes_head=True,shape='full',head_width=.1,color='red'  ,width=0.009)

p.text(2*6+3 ,-1-2.5,r"$\Lambda_A$",fontsize=38,color='blue')
p.text(2*32-9,-1-2.5,r"$\Lambda_D$",fontsize=38,color='green')
p.text(2*91-7,-1-2.5,r"$\Lambda_R$",fontsize=38,color='red')

p.plot((180,220),(SS-2.5,SS-2.5),'k--')





ax2 = ax.twinx()
#ax2.set_ylabel('Y values for ln(x)');
p.ylim(-3.8,1.8)


p.yticks((-1-2.5,0-2.5,SS-2.5,1-2.5),(-1,0,r"$a_S$",1),fontsize=26)






















p.show()

