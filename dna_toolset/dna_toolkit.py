from structures import nucleotides, dna_reverse_compliment
from utilities import colored


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
            nuc_count[nuc] = 1
    return nuc_count


def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T", "U")


def reverse_compliment(seq):
    """ 
    Swapping adenine with thymine and guanine with cytosine. 
    Reversing newly generated string 
    """
    # return ''.join([dna_reverse_compliment[nuc] for nuc in seq])[::-1]

    # Pythonic approach. A little bit faster
    mapping = str.maketrans('ATCG', 'TACG')
    return seq.translate(mapping)[::-1]


def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def gc_content_subsection(seq, k=20):
    """GC Content in subsection of DNA/RNA Sequences"""

    res = []
    for i in range(0, len(seq) - k+1, k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res
