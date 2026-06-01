allowed_amino_acids = set("ACDEFGHIKLMNPQRSTVWY")

file_path = "data/your_file_name.fasta"

header = ""
sequence_lines = []

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if not header:
                header = line
        else:
            sequence_lines.append(line)

sequence = "".join(sequence_lines).upper()

if not sequence:
    print("Error: no sequence found in the FASTA file.")
elif all(residue in allowed_amino_acids for residue in sequence):
    print("FASTA header:", header)
    print("Valid amino acid sequence.")
    print("Sequence length:", len(sequence))
    print("Predicted binding pocket: placeholder result")
    print("Possible effect on ammonium transport: placeholder interpretation")
else:
    print("Error: invalid sequence in FASTA file. Use only standard amino acid letters.")
