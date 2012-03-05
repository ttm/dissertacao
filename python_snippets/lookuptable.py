T=len(table)
SI= freq * T / 44100
ap=0
samples=[]
for i in xrange(int(dur*44100)):
    samples.append(table[int(ap)])
    ap = (SI + ap)
