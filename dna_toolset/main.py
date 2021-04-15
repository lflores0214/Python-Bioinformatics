# DNA Toolkit/Code testing file
from dna_toolkit import nucleotides, validate_sequence, count_nucleotides
import random

dna_str = ''.join([random.choice(nucleotides)
                   for _ in range(50)])

DNA_STR = validate_sequence(dna_str)


print(DNA_STR,"\n", count_nucleotides(DNA_STR))
