#-*- coding: utf8 -*-
import numpy as n, pylab as p

resolucao=9*8 # 72
#axL = p.subplot(2,1,1)
fig=p.figure()
ax1=fig.add_subplot(111)
ax2=ax1.twinx()

#p.plot((0,34),(1,1)); p.plot((36,72),(1,1))

#p.plot((0,16),(2,2)); p.plot((36,52),(2,2))
#p.plot((18,34),(2,2)); p.plot((54,72),(2,2))

ordem=[0,1,4,2,-1,5,-2,3,6]
colors=['g','b','r','b','k','r','k','b','r']

for i in xrange(9):
    for j in xrange(i+1):
        p.plot((j*resolucao/(i+1), (j+1)*resolucao/(i+1)-2),(ordem[i],ordem[i]),c=colors[i%len(colors)], linewidth=3)

p.plot((-1000,-1000),'r',linewidth=3,label=u'compassos compostos, divisões ternárias, modo perfeito')
p.plot((-1000,-1000),'b',linewidth=3,label=u'compassos simples, divisões binárias, modo imperfeito')
p.plot((-1000,-1000),'k',linewidth=3,label=u'compassos complexos em 5 e 7, quiálteras de 5 e 7')
p.legend(loc="upper right")


ax1.set_ylim(-3,8)
ax2.set_ylim(-3,8)
p.xlim(-4,74)

ax1.set_xticks(())
ax1.set_ylabel(r"$\leftarrow$"+u"divisões do pulso musical"+r"$\rightarrow$", fontsize=22)
ax2.set_ylabel(r"$\leftarrow$"+u"fórmulas de compasso"+r"$\rightarrow$", fontsize=22)

ax1.set_yticks((-2,-1,0,1,2,3,4,5,6))
ax1.set_yticklabels((r"$heptina\;de\;semicolcheia$",r"$quintina\;de\;semicolcheia$",r"$seminima$",r"$duas\;colcheias$",r"$quatro\;semicolcheias$",r"$oito\;fusas$", r"$tercina\;de\;colcheias$",r"$sextina\;de\;semicolcheias$",r"$nonina\;de\;semicolcheias$"), fontsize=18)

ax2.set_yticks((-2,-1,0,1,2,3,4,5,6))
ax2.set_yticklabels((r"$\binom{7}{4}$",r"$\binom{5}{4}$",r"$\binom{1}{4}$",r"$\binom{2}{4}$",r"$\binom{4}{4}$",r"$\binom{8}{4}$",r"$\binom{3}{4}$",r"$\binom{6}{8}$",r"$\binom{9}{8}$"), fontsize=22)
#axR=p.subplot(2,1,2,sharex=axL, frameon=False)
#axR.yaxis.set_label_position("right")

#ax.yaxis.set_ticks_position("right")
#axR.yaxis.tick_right()


#p.yticks((-1,0,1,2,3,4,5,6),(r"$-\delta_a$",r"$0$",r"$\delta_a$",r"$2\delta_a$",r"$3\delta_a$",r"$4\delta_a$",r"$5\delta_a$",r"$6\delta_a$"))

#p.ylabel(r"amplitude $\rightarrow$")
ax1.set_xlabel(r"tempo $\rightarrow$",fontsize=22)
p.show()

