from dna_toolset.structures import (
    nucleotides, dna_reverse_compliment, dna_codons)
from collections import Counter


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


def translate_seq(seq, init_pos=0):
    """
    Translates a DNA sequence into an aminoacid sequence
    """
    return [dna_codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq)-2, 3)]


def codon_usage(seq, aminoacid):
    """
    Provides the frequency of each codon encoding a given aminoacid in a DNA sequence
    """
    tmp_list = []

    for i in range(0, len(seq)-2, 3):
        if dna_codons[seq[i:i+3]] == aminoacid:
            tmp_list.append(seq[i:i+3])

    freq_dict = dict(Counter(tmp_list))
    total_weight = sum(freq_dict.values())

    for seq in freq_dict:
        freq_dict[seq] = round(freq_dict[seq] / total_weight, 2)

    return freq_dict


def gen_reading_frames(seq):
    """
    Generate the six reading frames of a DNA sequence, including the reverse compliment
    """
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_compliment(seq), 0))
    frames.append(translate_seq(reverse_compliment(seq), 1))
    frames.append(translate_seq(reverse_compliment(seq), 2))
    return frames
