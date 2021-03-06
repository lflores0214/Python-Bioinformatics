dna_reverse_compliment = {"A": "T",
                          "T": "A",
                          "C": "G",
                          "G": "C"}


def reverse_compliment(seq):
    """ Swapping adenine with thymine and guanine with cytosine. Reversing newly generated string """
    return ''.join([dna_reverse_compliment[nuc] for nuc in seq])[::-1]


dna_seq = "GAAGGTTAACGGTCTCTACGTGTCGCAACGCTAGTTTATATCAAGAATAGTGATCCCCATTAATGAAGTCACACGTCTGGGAATCTGAAGAAGGCGCCATTTTCCATAGAGGGTTAAGGATTGAGGTGAGTGTCCGTCACACCTCCGCCACGCGTGACCGACGTACCTATAGTTAAGAGTTACTTACGAGTAGAACGATCAGAGAAATTTCGTGTAGTCACCTAACAGATGGAATTACTACTAACTAAGTGCCTGTGAGTGTCCTAACTACCTAGGGTACCCCTTAGTAATCATTCGGTTTTTATGCGAAGCACTGTCCCACTTTGCGGGGACCGCAGACCTAGCGTATTTATGACATCCCTTCTGCAAGGGCGCCAACACGCACGACAGCATGTTTAGTTGGAGCTTCCAAGTCAACCCCGCAACAGTTCTGGCTCCAAATACTGTTACAGTCTTAAAAGCATAAGGATCACGACTAACCACAATGCCGGGCCTAATCTTTCTTAGTTACACGCGATAAAGTTTGCCCTAATAACGTGGGCCTCACATAAATGGCAAACGAGTGTGCCCCTTGCTTCAGATCAAAAAGAGGGCACGACACAGAGACGACAGGGGTGATAGCGAAGCCAATGGTTGGGCATAAAAAATAACTAACTGCCAGAGATCTCTGGATCTAAACACACGAAAACGCCGGAATACGAGTGCACGGGACCGGTTATCTATCCCCGTAAATAAGATACCGAGACCGGTGAGAGCCCAATATATGCGGTCTGAGGGCAGGTCGGTATAAAGAAGGCCGTGGTGCCTGCCTTCAAAAACCTTGCCCAATGATGCTTGCGCACTAAGAGTGGATCAGTGCGACCGGTTGGATGTAGGTGGGGCGCTTGTTTTAGCGCGCTGT"

print(reverse_compliment(dna_seq))
