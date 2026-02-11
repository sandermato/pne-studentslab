
def first(seq):
    list = ""
    for i in range(0,5):
        list += seq[i]
    return list

def last(seq):
    list2 = ""
    for i in range(len(seq)-3,len(seq)):
        list2 += seq[i]
    return list2

def check_substring(seq):
    i = 0
    total = 0
    while i < len(seq):
        if seq[i] == 'A' and i < len(seq)-2:
            if (seq[i+1] == 'T') and (seq[i+2] == 'C'):
                total += 1
        i += 1
    return total

if __name__ == "__main__":
    dna = "ATGCGATCGATCGATCGATCGA"
    rna = dna.replace('T', 'U')
    print("Length:", len(dna))
    print("First 5:", first(dna))
    print("Last 3:", last(dna))
    print("Lowercase:", dna.lower())
    print("ATC count:", check_substring(dna))
    print("RNA:", rna)