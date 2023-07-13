from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import DataStructs
import numpy as np 
import sys
np.set_printoptions(threshold=sys.maxsize)


def one_hot_encode_molecule(smiles):
    # Create an RDKit molecule object from the SMILES string
    molecule = Chem.MolFromSmiles(smiles)
    
    # Generate Morgan fingerprint for the molecule
    fingerprint = AllChem.GetMorganFingerprintAsBitVect(molecule, 2, nBits=1024)
    fingerprint2 = np.array(fingerprint)
    fingerprint2 = fingerprint2.tolist()
    final1 = "".join(str(fingerprint2))
    # print(fingerprint2)
    # Convert the fingerprint to a one-hot encoded binary vector
    one_hot_vector = [int(bit) for bit in fingerprint.ToBitString()]
    # print(type(one_hot_vector))
    final_2 = "".join(str(one_hot_vector))

    print( final1 == final_2)
    return one_hot_vector
smiles = 'CC(=O)OC1=CC=CC=C1C(=O)O'

one_hot_encode_molecule(smiles=smiles)

#lowkey idk if this is right
