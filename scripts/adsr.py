#-*- coding: utf8 -*-
import numpy as n, pylab as p

ax=p.subplot(111)

De=2*100. #duracao total (\Delta)
DA=2*20. # duracao do ataque \Delta_A
DD=2*20. # duracao do decay \Delta_D
DR=2*20. # duracao do release \Delta_R
SS=.4 # fração da amplitude em que ocorre o sustain

A=2**(n.arange(DA)/(DA-1))-1 # amostras do ataque
s=n.copy(A) 
D=SS**(n.arange(DA,DA+DD)/DD-1) # amostras do decay
s=n.hstack((  s,  D  ))
S=SS*n.ones(De-DR-(DA+DD)) # amostras do sustain
s=n.hstack((  s, S  ))
R=(SS+1)*(1/(SS+1))**((n.arange(De-DR,De)+DR-De)/(DR))-1 # amostras do release
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
p.plot(som,'c*',markersize=9,label=u"Som amostrado submetido ao envelope ADSR")
p.plot(som,'c')

p.legend(loc="upper right",prop={'size':16})
p.xlim(-10,De+10)
p.ylim(-1.2,1.2)

p.yticks((-1,0,SS,1),(-1,0,r"$a_S$",1),fontsize=26)
p.xticks(())


p.arrow(0,-1.1,DA,0,length_includes_head=True,shape='full',head_width=.1,color='cyan'     ,width=0.009)
p.arrow(DA,-1.1,-DA,0,length_includes_head=True,shape='full',head_width=.1,color='blue'   ,width=0.009)  
p.arrow(DA+DD,-1.1,-DD,0,length_includes_head=True,shape='full',head_width=.1,color='cyan',width=0.009)
p.arrow(DA,-1.1,DD,0,length_includes_head=True,shape='full',head_width=.1,color='green'   ,width=0.009)
p.arrow(De,-1.1,-DR,0,length_includes_head=True,shape='full',head_width=.1,color='red'    ,width=0.009)
p.arrow(De-DR,-1.1,DR,0,length_includes_head=True,shape='full',head_width=.1,color='red'  ,width=0.009)

p.text(2*6+3 ,-1,r"$\Lambda_A$",fontsize=38,color='blue')
p.text(2*32-9,-1,r"$\Lambda_D$",fontsize=38,color='green')
p.text(2*91-7,-1,r"$\Lambda_R$",fontsize=38,color='red')

p.plot((-20,7),(SS,SS),'k--')

p.show()

