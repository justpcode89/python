amino_acids = 'ACDEFGHIKLMNPQRSTVWY'

amino_acid_weights = {
    'A': 89.09,  # Alanine
    'C': 121.15, # Cysteine
    'D': 133.10, # Aspartic Acid
    'E': 147.13, # Glutamic Acid
    'F': 165.19, # Phenylalanine
    'G': 75.07,  # Glycine
    'H': 155.16, # Histidine
    'I': 131.17, # Isoleucine
    'K': 146.19, # Lysine
    'L': 131.17, # Leucine
    'M': 149.21, # Methionine
    'N': 132.12, # Asparagine
    'P': 115.13, # Proline
    'Q': 146.15, # Glutamine
    'R': 174.20, # Arginine
    'S': 105.09, # Serine
    'T': 119.12, # Threonine
    'V': 117.15, # Valine
    'W': 204.23, # Tryptophan
    'Y': 181.19  # Tyrosine
}

# Kyte-Doolittle hydrophobicity scale for amino acids
hydrophobicity_scale = {
    'A': 1.8,  # Alanine
    'C': 2.5,  # Cysteine
    'D': -3.5, # Aspartic Acid
    'E': -3.5, # Glutamic Acid
    'F': 2.8,  # Phenylalanine
    'G': -0.4, # Glycine
    'H': -3.2, # Histidine
    'I': 4.5,  # Isoleucine
    'K': -3.9, # Lysine
    'L': 3.8,  # Leucine
    'M': 1.9,  # Methionine
    'N': -3.5, # Asparagine
    'P': -1.6, # Proline
    'Q': -3.5, # Glutamine
    'R': -4.5, # Arginine
    'S': -0.8, # Serine
    'T': -0.7, # Threonine
    'V': 4.2,  # Valine
    'W': -0.9, # Tryptophan
    'Y': -1.3  # Tyrosine
}

drug_data = [
    {"Drug Name": "Aspirin", "Molecular Weight": 180.16, "LogP": 1.2, "Bioavailability": 68, "Therapeutic Class": "Analgesic"},
    {"Drug Name": "Metformin", "Molecular Weight": 129.16, "LogP": -1.43, "Bioavailability": 50, "Therapeutic Class": "Antidiabetic"},
    {"Drug Name": "Ibuprofen", "Molecular Weight": 206.29, "LogP": 3.97, "Bioavailability": 80, "Therapeutic Class": "Anti-inflammatory"},
    {"Drug Name": "Atorvastatin", "Molecular Weight": 558.64, "LogP": 5.7, "Bioavailability": 12, "Therapeutic Class": "Antihyperlipidemic"},
    {"Drug Name": "Paracetamol", "Molecular Weight": 151.16, "LogP": 0.46, "Bioavailability": 85, "Therapeutic Class": "Analgesic"},
    {"Drug Name": "Ciprofloxacin", "Molecular Weight": 331.34, "LogP": -0.6, "Bioavailability": 70, "Therapeutic Class": "Antibiotic"},
    {"Drug Name": "Amoxicillin", "Molecular Weight": 365.4, "LogP": -0.8, "Bioavailability": 95, "Therapeutic Class": "Antibiotic"},
    {"Drug Name": "Omeprazole", "Molecular Weight": 345.42, "LogP": 2.3, "Bioavailability": 50, "Therapeutic Class": "Proton Pump Inhibitor"}
]
