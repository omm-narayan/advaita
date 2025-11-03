import torch
from torch.utils.data import Dataset

class SequenceDataset(Dataset):
    """Load and process DNA sequences for CRISPR guides"""
    
    def __init__(self, fasta_file, guide_positions, labels):
        self.genome = self._load_genome(fasta_file)
        self.guide_positions = guide_positions
        self.labels = labels
        
    def __len__(self):
        return len(self.guide_positions)
    
    def __getitem__(self, idx):
        # TODO: Implement sequence extraction
        sequence = self._extract_sequence(self.guide_positions[idx])
        label = self.labels[idx]
        return sequence, label
        
    def _load_genome(self, fasta_file):
        """Load reference genome"""
        # Implementation here
        pass 