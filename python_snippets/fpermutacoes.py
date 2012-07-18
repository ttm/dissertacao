class Permutation:
    """Simple permutation.
    
    see http://en.wikipedia.org/wiki/Permutation for nomenclature
    
    If one-line notation, it runs like:
    permuted=[original[i] for i in Permutation.one_line]
    
    If cycle notation:
    unfold to one-line notation
    
    note
    one_line = (2,3,1) # is equivalent to
    cycle=(1,2,3)
    
    one_line=(2,5,4,3,1) # is equivalent to
    cycle=(1,2,5)(3,4)"""
    def __init__(self, one_line=(2,3,1)):
        self.one_line = one_line
        self.size=len(one_line)
        

class PermutationPattern(Permutation):
    """A Permutation with periodicity/incidence_index information"""
    period=1
    def changePeriodicity(self, new_val=1):
        self.period=new_val

