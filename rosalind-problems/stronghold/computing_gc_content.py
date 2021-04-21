def read_file(file):
    """
    Read a file and return a list of lines
    """
    with open(file, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return round(
        ((seq.count('C') + seq.count('G')) / len(seq) * 100), 6)


#== Read data from file (FASTA formated file) ==#
fasta_file = read_file("test_data/gc_content.txt")

# Dictionary for Labels + Data
fasta_dict = {}
# String holing the current label
fasta_label = ""

# == Clean & Prepare the data (Format for ease of use with our gc_content fn)
# Converting FAFSTA file into a dictionary
for line in fasta_file:
    if '>' in line:
        fasta_label = line[1:]
        fasta_dict[fasta_label] = ""
    else:
        fasta_dict[fasta_label] += line

# == Format the data (Store the data in a convenient way)
# == Run need operations on data (Pass data into gc_content fn)
# Using dictionary comprehension generate a new dict with results
result_dict = {key: gc_content(value) for (key, value) in fasta_dict.items()}

max_gc_key = max(result_dict, key=result_dict.get)

# == Collect results

print(f'{max_gc_key}\n{result_dict[max_gc_key]}')
