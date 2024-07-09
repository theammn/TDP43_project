import matplotlib.pyplot as plt
import csv

def read_identity_scores(file_path):
    identity_results = {}
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            protein, score = row
            identity_results[protein] = float(score)
    return identity_results

def visualize_sequence_identity(identity_results, save_path=None):
    proteins = list(identity_results.keys())
    identities = list(identity_results.values())

    plt.figure(figsize=(10, 6))
    plt.bar(proteins, identities, color='skyblue')
    plt.xlabel('Proteins')
    plt.ylabel('Sequence Identity (%)')
    plt.title('Sequence Identity between TDP43 and Other Proteins')
    plt.ylim(0, 100)  # Set y-axis limit from 0 to 100%
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    for i, v in enumerate(identities):
        plt.text(i, v + 1, f"{v:.2f}%", ha='center', va='bottom')

    if save_path:
        plt.savefig(save_path)
        print(f"Figure saved as {save_path}")

    plt.show()

if __name__ == "__main__":
    file_path = 'identity_scores.csv'  # Path to the CSV file with identity scores
    identity_results = read_identity_scores(file_path)
    save_path = 'sequence_identity_plot.png'  # Path to save the plot image
    visualize_sequence_identity(identity_results, save_path)
