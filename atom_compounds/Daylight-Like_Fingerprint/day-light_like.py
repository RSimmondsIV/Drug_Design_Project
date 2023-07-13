from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator

def encode_smiles(smiles):
    # Convert SMILES string to RDKit molecule object
    molecule = Chem.MolFromSmiles(smiles)

    # Create Daylight-like fingerprint generator
    generator = rdFingerprintGenerator.GetDaylightFingerprintGenerator()

    # Generate fingerprint
    fingerprint = generator.GetFingerprint(molecule)

    # Convert fingerprint to binary string representation
    fingerprint_binary = fingerprint.ToBitString()

    return fingerprint_binary

# Example usage
smiles = 'CC(=O)OC1=CC=CC=C1C(=O)O'
fingerprint = encode_smiles(smiles)
print(fingerprint)