from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs

def one_hot_encode_molecule(smiles):
    # Create an RDKit molecule object from the SMILES string
    molecule = Chem.MolFromSmiles(smiles)
    
    # Generate Morgan fingerprint for the molecule
    fingerprint = AllChem.GetMorganFingerprintAsBitVect(molecule, 2, nBits=1024)
    
    # Convert the fingerprint to a one-hot encoded binary vector
    one_hot_vector = [int(bit) for bit in fingerprint.ToBitString()]
    
    return one_hot_vector
smiles = 'CC(=O)OC1=CC=CC=C1C(=O)O'

one_hot_vector = one_hot_encode_molecule(smiles)
print(one_hot_vector)