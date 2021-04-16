def colored(seq):
    bcolors = {
        "A": "\033[92m",
        "C": "\033[94m",
        "G": "\033[93m",
        "T": "\033[91m",
        "U": "\033[91m",
        "reset": "\033[0;0m",
    }
    tmp_str = ""
    for nuc in seq:
        if nuc in bcolors:
            tmp_str += bcolors[nuc] + nuc
        else:
            tmp_str += bcolors['reset'] + nuc
    return tmp_str + '\033[0;0m'
