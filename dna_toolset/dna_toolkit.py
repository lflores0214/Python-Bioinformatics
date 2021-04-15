nucleotides = ["A", "T", "C", "G"]


def validate_sequence(dna_seq):
    temp_seq = dna_seq.upper()
    for nuc in temp_seq:
        if nuc not in nucleotides:
            return False
    return temp_seq


def count_nucleotides(dna_seq):
    temp_seq = dna_seq.upper()
    nuc_count = {}
    for nuc in temp_seq:
        if nuc in nuc_count:
            nuc_count[nuc] += 1
        else:
            nuc_count[nuc] = 0
    return nuc_count
