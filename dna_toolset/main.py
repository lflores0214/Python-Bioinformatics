# DNA Toolkit/Code testing file
from dna_toolkit import transcription, nucleotides, validate_sequence, count_nucleotides, reverse_compliment
from utilities import colored
import random

dna_str = ''.join([random.choice(nucleotides)
                   for _ in range(50)])

DNA_STR = validate_sequence(dna_str)


print(f"\nSequence: {colored(DNA_STR)}")
print(f"[1] + Sequence Length: {len(DNA_STR)} \n")
print(f"[2] + Nucleotide Frequency  : {count_nucleotides(DNA_STR)} \n")
print(f"[3] + DNA/RNA Transcription : {colored(transcription(DNA_STR))}\n")
print(f"[4] + Reverse Compliment    : {colored(reverse_compliment(DNA_STR))}\n")
