# RNA-Binding Motifs in Human TDP43 and Its Interactors

This project aims to identify RNA-binding motifs in the human TDP43 protein and compare these motifs to those found in proteins that interact with TDP43. By analyzing the conservation of these motifs across different interactors, we can gain insights into their functional significance in RNA-protein interactions.

# Goals:
1. Identify RNA-binding motifs in the human TDP43 protein.
2. Analyze the conservation of these motifs in the interactors of TDP43.
3. Compare conservation scores to understand how well these motifs are preserved across different interacting proteins.
4. Identify commonly conserved motifs that are shared between human TDP43 and its interactors.

As input, we will have msas files from TDP43 and few targeted interactors.
We try now to identify RNA-Binding Motifs and search for these motifs in the sequences of human TDP43 and its interactors, in order to then calculate conservation scores

# Methodology:

- Load MSA Data: Read the MSA files for human TDP43 and its interactors.
- Identify RNA-Binding Motifs: Search for known RNA-binding motifs (e.g., 'UGG') in the sequences.
- Calculate Conservation Scores: Analyze how conserved these motifs are across all sequences in the MSA files.
- Compare Conservation Across Interactors: Compare the conservation scores of RNA-binding motifs between human TDP43 and its interactors.
- Identify Commonly Conserved Motifs: Highlight motifs that are highly conserved in both human TDP43 and its interactors.
- Save Results: Export the identified motifs and their conservation scores to CSV files for further analysis.

# Structure:
Input : MSA (Multiple Sequence Alignment) files for human TDP43 and its targeted interactors (fasta files)

Script : analyze_rna_binding_motifs.py
