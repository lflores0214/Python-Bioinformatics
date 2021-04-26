
import dna_toolset.bio_structs as structs
import random
from collections import Counter


class BioSeq:
    """
    DNA sequence class. Default value ATCG, DNA, No label
    """

    def __init__(self, seq="ATCG", seq_type="DNA", label="No Label"):
        self.seq = seq.upper()
        self.label = label
        self.seq_type = seq_type
        self.is_valid = self.__validate()
        assert self.is_valid, f"Provided data does not seem to be correct {self.seq_type} sequence"

    def __validate(self) -> bool:
        """
        Check the sequence to make sure it is a valid DNA string
        """
        return set(structs.dna_nucleotides).issuperset(self.seq)

    def get_seq_biotype(self) -> str:
        """
        Returns sequence type
        """
        return self.seq_type

    def get_seq_info(self) -> str:
        """
        Returns 4 strings. Full sequence information.
        """
        return f"[Label] {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Length]: {len(self.seq)}"

    def generate_rand_seq(self, length=10, seq_type="DNA") -> None:
        """
        Generate a random DNA sequence.
        Provide the length and seq_type.
        Default length is 10.
        Default seq_type is DNA
        """
        seq = ''.join([random.choice(structs.dna_nucleotides)
                      for _ in range(length)])
        self.__init__(seq, seq_type, "Randomly generated sequence")

    def count_nucleotides(self) -> dict:
        """
        Provides the frequency of each nucleotide in the DNA sequence.
        """
        count = Counter(self.seq)
        return count

    def transcription(self) -> str:
        """
        DNA -> RNA Transcription. Replaces thymine (T) with uracil (U)
        """
        rna = self.seq.replace("T", "U")
        return rna

    def reverse_compliment(self) -> str:
        """
        Swaps adenine (A) with thymine (T) and guanine (G) with cytosine (C). 
        The new string is then reversed and returned. 
        """
        mapping = str.maketrans('ATCG', 'TACG')
        return self.seq.translate(mapping)[::-1]

    def gc_content(self, seq) -> float:
        """
        CG content in a given DNA or RNA sequence
        """
        if seq is None:
            seq = self.seq
        return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

    def gc_content_subsection(self, seq, k=20) -> list:
        """
        GC content in a subsection of a given DNA or RNA sequence
        """
        res = []
        for i in range(0, len(self.seq) - k+1, k):
            subseq = seq[i:i+k]
            gc_content = self.gc_content(subseq)
            res.append(gc_content)
        return res

    def translate_seq(self, init_pos=0) -> list:
        """
        Translates the DNA sequence into an aminoacid sequence
        """
        return [structs.dna_codons[self.seq[pos:pos + 3]] for pos in range(init_pos, len(self.seq)-2, 3)]

    def codon_usage(self, aminoacid) -> dict:
        """
        Provides the frequency of each codon encoding a given aminoacid in the DNA sequence.
        """
        tmp_list = []

        for i in range(0, len(self.seq)-2, 3):
            if structs.dna_codons[self.seq[i:i+3]] == aminoacid:
                tmp_list.append(self.seq[i:i+3])
        freq_dict = dict(Counter(tmp_list))
        total_weight = sum(freq_dict.values())

        for seq in freq_dict:
            freq_dict[seq] = round(freq_dict[seq] / total_weight, 2)

        return freq_dict

    # def gen_reading_frames(self):
    #     frames = []
    #     frames.append(self.translate_seq(0))
    #     frames.append(self.translate_seq(1))
    #     frames.append(self.translate_seq(2))
    #     frames.append(self.translate_seq(self.reverse_compliment(), 0))
    #     frames.append(self.translate_seq(self.reverse_compliment()))
    #     frames.append(self.translate_seq(self.reverse_compliment()))
      