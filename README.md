# Sequence Identity Analysis Algorithm for Protein Interactions in ALS Research, focusing on Human TDP43 and Its Interactors

TDP43, or TAR DNA-binding protein 43, holds a crucial role in the complex landscape of Amyotrophic Lateral Sclerosis (ALS), a disease that strikes at the very core of motor neuron function. Understanding its interactions with other proteins is vital for unraveling the mysteries of ALS pathology.

In my research, I focus on identifying proteins that potentially interact with TDP43. These interactions could provide key insights into how TDP43 influences ALS progression. By examining the pairwise identity between TDP43 and various candidate proteins, I aim to uncover commonalities and distinctions in their amino acid sequences.

Pairwise identity, essentially the percentage of identical amino acids between two protein sequences, offers valuable clues about their evolutionary relationships and functional similarities. This comparative analysis is crucial for deciphering how these proteins might cooperate or compete in cellular processes related to ALS.

Through this study, I hope to contribute to our understanding of ALS at a molecular level. Ultimately, my goal is to pinpoint new avenues for therapeutic intervention or diagnostic strategies, bringing us closer to effective treatments for this devastating neurological disorder.

# Goals:
1. Identify Sequence Identity: Compare the sequence identity between the human TDP43 protein and its potential interactors from multiple sequence alignment (MSA) files.
2. Understand Conservation: Analyze how conserved specific proteins are across different interactions with TDP43.

As input, we will have msas files from TDP43 and few targeted interactors.

# Methodology:

- Load MSA Data: Read the MSA files for human TDP43 and its interactors.
- Identify the sequences.
- Calculate Conservation Scores: Analyze how conserved motifs are across all sequences in the MSA files.
- Calculate the scores of identity between TDP43 and the interactors

# Structure:
Input : MSA (Multiple Sequence Alignment) files for human TDP43 and its targeted interactors (fasta files)

Script : identity.py
