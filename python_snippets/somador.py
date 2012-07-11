def somador(seq1,seq2):
    # Basicamente adiciona zeros na sequencia menor para somar rapidamente
    diff=len(seq1)-len(seq2)
    if diff > 0:
        seq2+=[0]*diff
    elif diff< 0:
        seq1+=[0]*-diff
        
    seq=[(i+j) for i,j in zip(seq1,seq2)]
    return seq
