import os
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import SeqIO
import csv

def read_fasta(file_path):
    sequences = {}
    for record in SeqIO.parse(file_path, "fasta"):
        sequences[record.id] = str(record.seq)
    return sequences

def process_fasta_files(tdp43_file, proteins_file):
    tdp43_sequences = read_fasta(tdp43_file)
    proteins_sequences = read_fasta(proteins_file)

    if not tdp43_sequences or 'TDP43' not in tdp43_sequences:
        print("TDP43 sequence not found in the specified file.")
        return
    
    tdp43_sequence = tdp43_sequences['TDP43']
    identity_results = {}

    for header, sequence in proteins_sequences.items():
        identity = calculate_identity(tdp43_sequence, sequence)
        identity_results[header] = identity
        print(f"Sequence Identity between TDP43 and {header}: {identity:.2f}%")
    
    save_identity_scores(identity_results)

def calculate_identity(sequence1, sequence2):
    alignments = pairwise2.align.globalxx(sequence1, sequence2)
    top_alignment = alignments[0]  # Take the top alignment (best score)
    aligned_sequence1, aligned_sequence2, score, begin, end = top_alignment
    identity = (score / len(sequence1)) * 100  # Calculate percentage identity
    return identity

def save_identity_scores(identity_results):
    with open('identity_scores.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Protein", "Identity Score"])
        for protein, score in identity_results.items():
            writer.writerow([protein, score])
    print("Identity scores saved to identity_scores.csv")

if __name__ == "__main__":
    tdp43_file = '/home/labs/hornsteinlab/theam/MLcourse/assignments/project/final/tdp43.fasta'  # Update this path to the TDP43 fasta file
    proteins_file = '/home/labs/hornsteinlab/theam/MLcourse/assignments/project/final/proteins.fasta'  # Update this path to the proteins fasta file
    process_fasta_files(tdp43_file, proteins_file)
