T=2048
senoide=np.sin(np.linspace(0,2*np.pi,T,endpoint=False))
dente=np.linspace(-1,1,T,endpoint=False)
triangular=np.hstack((dente[::2],dente[-1:0:-2]))
quadrada=np.hstack((np.ones(T/2),np.ones(T/2)*-1))
