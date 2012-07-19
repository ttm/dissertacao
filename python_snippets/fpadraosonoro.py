class Pattern:
    """Sequence with PermutationPattern classes applied successively
    
    Parameters
    ----------
    sequence : class
      An instantiated FIGGUS Sequence class
    permutation_pattern : class
      An instantiated FIGGUS PermutationPattern class"""
    def __init__(self, sequence=Sequence(), permutation_pattern=PermutationPattern(),iterations=1):
        self.unit_count=sequence.unit_count * iterations
        self.sequence=sequence
        self.permutation_pattern=permutation_pattern
        
	    self.tail=sequence.unit_count - permutation_pattern.size
        if sequence.unit_count > permutation_pattern.size:
	        self.tail_elements = range(permutation_pattern.size,sequence.unit_count)
        else:
	        self.tail_elements = []
        
        pattern=[sequence.active_grains]
        stage=sequence.active_grains
	    for i in xrange(iterations-1):
	        if i%permutation_pattern.period == 0:
		        stage = [stage[j-1] for j in permutation_pattern.one_line]
		        stage += self.tail_elements
		        pattern.append(stage)
	        else:
		        pattern.append(stage)
	    self.pattern=pattern # lista de listas que sao as posicoes em cada compasso
	    self.initFileSpecs()

    def initFileSpecs(self):
	    self.SR=44100
	    self.N=1024 #utilizado na classe Tables

    def synthesizeSonicVectors(self):
    	sonic_vector=[]
	
    	for compass in self.pattern:
    	    units=[ self.sequence.ordered_unit_grains[position] for position in compass]
    	    compass_vector=[]
	    for unit in units:
		    SI= unit.freq * self.N / self.SR
		    ap=0
		for i in xrange(int(unit.duration*self.SR)):
		    sonic_vector.append(unit.intensidade*Tables.sin1024[int(ap)])
		    ap = (SI + ap)%self.N
	    self.sonic_vector=sonic_vector
	    self.sonic_vector2=[] # Always MONO for now.
