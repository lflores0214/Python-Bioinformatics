# DNA Toolkit/Code testing file
from dna_toolkit import (transcription, nucleotides, validate_sequence,
                         count_nucleotides, reverse_compliment, gc_content, gc_content_subsection,
                         translate_seq, codon_usage)
from utilities import colored
import random

dna_str = ''.join([random.choice(nucleotides)
                   for _ in range(50)])

DNA_STR = validate_sequence(dna_str)


print(f"\nSequence: {colored(DNA_STR)}")
print(f"[1] + Sequence Length: {len(DNA_STR)} \n")
print(f"[2] + Nucleotide Frequency  : {count_nucleotides(DNA_STR)} \n")
print(f"[3] + DNA/RNA Transcription : {colored(transcription(DNA_STR))}\n")
print(
    f"[4] + DNA string + Compliment + Reverse Compliment: \n5' {colored(reverse_compliment(DNA_STR))} 3'")
print(f"3' {colored(reverse_compliment(DNA_STR)[::-1])} 5' [Compliment]")
print(f"5' {colored(reverse_compliment(DNA_STR))} 3' [Reverse Compliment]")
print(f"[5] + GC Content : {gc_content(DNA_STR)}%")
print(
    f"[6] + GC Content in subsection k=5 : {gc_content_subsection(DNA_STR, k=5)}\n")
print(f"[7] + Aminoacids Sequence from DNA:{translate_seq(DNA_STR, 0)}\n")
print(f"[8] + Codon Frequency (L): {codon_usage(DNA_STR, 'L')}\n")
