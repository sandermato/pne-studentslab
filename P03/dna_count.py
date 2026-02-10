
def counting(sequence):
    i = 0
    length = len(sequence)
    A = 0
    C = 0
    T = 0
    G = 0
    while i < len(sequence):
        if sequence[i] == 'A':
            A += 1
        elif sequence[i] == 'C':
            C += 1
        elif sequence[i] == 'T':
            T += 1
        elif sequence[i] == 'G':
            G += 1
        i += 1
    return length, A, C, T, G

seq = input("Introduce the sequence: ")
length, A, C, T, G = counting(seq)
print("The total length is:", length, "\nA:", A, "\nC:", C, "\nT:", T, "\nG:", G)

