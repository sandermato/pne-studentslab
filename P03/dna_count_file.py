
def total(content):
    i = 0
    total_bases = 0
    while i < len(content):
        total_bases += len(content[i])
        i += 1
    return total_bases

def different(content):
    A = 0
    C = 0
    T = 0
    G = 0
    for I in range(0, len(content)):
        i = 0
        new = content[I]
        while i < len(new):
            if new[i] == 'A':
                A += 1
            elif new[i] == 'C':
                C += 1
            elif new[i] == 'T':
                T += 1
            elif new[i] == 'G':
                G += 1
            i += 1
    return A, C, T, G

with open('dna.txt') as r:
    contents = r.readlines()
print("\nNumber of total bases:", total(contents))
A, C, T, G = different(contents)
print("\nA:", A, "\nC:", C, "\nT:", T, "\nG:", G)