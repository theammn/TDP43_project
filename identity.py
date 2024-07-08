import os
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

def read_a3m(file_path):
    with open(file_path, 'r') as file:
        sequences = {}
        header = ""
        sequence = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if header and sequence:
                    sequences[header] = sequence
                header = line[1:]  # Remove the '>'
                sequence = ""
            elif not line.startswith("#"):  # Skip comments
                sequence += line.replace('.', '')  # Remove dots for alignments
        if header and sequence:
            sequences[header] = sequence
    return sequences

def process_a3m_folder(folder_path):
    all_sequences = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".a3m"):
            file_path = os.path.join(folder_path, filename)
            sequences = read_a3m(file_path)
            if sequences:
                header, sequence = next(iter(sequences.items()))  # Get the first sequence
                all_sequences[header] = sequence
            print(f"Processed {filename} with {len(sequences)} sequences.")
    return all_sequences

def main(folder_path):
    all_sequences = process_a3m_folder(folder_path)
    
    # Example: Print the first sequence of each file
    for header, sequence in all_sequences.items():
        print(f"Header: {header}\nSequence: {sequence[:60]}...\n")
    
    # Compare TDP43 with each sequence in all_sequences
    if 'TDP43' in all_sequences:
        sequence_tdp43 = all_sequences['TDP43']
        for header, sequence in all_sequences.items():
            if header != 'TDP43':  # Skip comparing TDP43 with itself
                identity = calculate_identity(sequence_tdp43, sequence)
                print(f"Sequence Identity between TDP43 and {header}: {identity:.2f}%")

def calculate_identity(sequence1, sequence2):
    alignments = pairwise2.align.globalxx(sequence1, sequence2)
    top_alignment = alignments[0]  # Take the top alignment (best score)
    aligned_sequence1, aligned_sequence2, score, begin, end = top_alignment
    identity = (score / len(sequence1)) * 100  # Calculate percentage identity
    return identity

if __name__ == "__main__":
    folder_path = 'msa'
    main(folder_path)
